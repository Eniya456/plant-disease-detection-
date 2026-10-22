import os
import uuid
from functools import wraps
from pathlib import Path
from flask import (
    Flask, render_template, request, redirect, url_for, 
    session, flash, send_from_directory, jsonify, abort
)
from werkzeug.utils import secure_filename

from config import Config
from database.db import (
    init_db, create_user, authenticate_user, get_user_by_id,
    save_prediction, get_user_predictions, get_prediction_by_id,
    get_user_stats, clear_user_predictions, delete_prediction_by_id
)
from ml.predictor import predict_leaf_disease, get_model_status
from ml.disease_catalog import (
    DISEASE_CATALOG, get_disease_info, get_all_categories,
    get_categories_by_group, get_ml_supported_categories, get_reference_only_categories
)

# Initialize Flask application
app = Flask(__name__)
app.config.from_object(Config)

# Ensure required runtime folders exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(os.path.dirname(app.config['DATABASE_PATH']), exist_ok=True)

# Initialize database schema and default demo account
with app.app_context():
    init_db()

# ----------------- Decorators & Helpers -----------------

def login_required(f):
    """Restricts access to authenticated users only."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash("Please sign in to access this page.", "warning")
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

def allowed_file(filename):
    """Check if uploaded file has a permissible extension."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

# ----------------- Core Routes -----------------

@app.route('/')
def index():
    """Public landing page."""
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration route."""
    if 'user_id' in session:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        full_name = request.form.get('full_name', '').strip()
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')

        # Basic validations
        if not username or not email or not password:
            flash("All required fields must be filled.", "danger")
            return render_template('register.html')

        if len(username) < 3:
            flash("Username must be at least 3 characters long.", "danger")
            return render_template('register.html')

        if len(password) < 6:
            flash("Password must be at least 6 characters long.", "danger")
            return render_template('register.html')

        if password != confirm_password:
            flash("Passwords do not match.", "danger")
            return render_template('register.html')

        result = create_user(username, email, password, full_name)
        if result['success']:
            flash("Account registered successfully! You may now sign in.", "success")
            return redirect(url_for('login'))
        else:
            flash(result.get('error', 'Registration failed.'), "danger")

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """User authentication route."""
    if 'user_id' in session:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        identifier = request.form.get('identifier', '').strip()
        password = request.form.get('password', '')

        if not identifier or not password:
            flash("Please provide your username/email and password.", "danger")
            return render_template('login.html')

        user = authenticate_user(identifier, password)
        if user:
            session.clear()
            session['user_id'] = user['id']
            session['username'] = user['username']
            session['full_name'] = user['full_name']
            session['email'] = user['email']
            flash(f"Welcome back, {user['full_name'] or user['username']}!", "success")

            next_page = request.args.get('next')
            if next_page and next_page.startswith('/'):
                return redirect(next_page)
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid username/email or password.", "danger")

    return render_template('login.html')

@app.route('/logout')
def logout():
    """User logout."""
    session.clear()
    flash("You have been signed out.", "info")
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    """Main authenticated analytical dashboard."""
    user_id = session['user_id']
    stats = get_user_stats(user_id)
    recent = get_user_predictions(user_id, limit=5)
    return render_template('dashboard.html', stats=stats, recent_predictions=recent)

@app.route('/detect', methods=['GET', 'POST'])
@login_required
def detect():
    """Leaf disease detection and diagnosis endpoint."""
    user_id = session['user_id']
    view_id = request.args.get('view_id')

    # If inspecting an existing past prediction from history or dashboard
    if request.method == 'GET' and view_id:
        try:
            pred = get_prediction_by_id(int(view_id), user_id)
            if pred:
                disease_info = get_disease_info(pred['predicted_class'])
                result = {
                    "predicted_class": pred['predicted_class'],
                    "confidence": pred['confidence'],
                    "confidence_pct": f"{round(pred['confidence'] * 100, 1)}%",
                    "probabilities": {pred['predicted_class']: pred['confidence']},
                    "is_healthy": bool(pred['is_healthy']),
                    "is_demo": bool(pred['is_demo']),
                    "disease_info": disease_info,
                    "error": None
                }
                img_url = url_for('uploaded_file', filename=pred['filename'])
                return render_template('detect.html', result=result, uploaded_image_url=img_url)
        except Exception as e:
            flash("Could not locate requested scan record.", "warning")

    if request.method == 'POST':
        file = request.files.get('leaf_image')
        sample_name = request.form.get('sample_name', '').strip()

        # Handle either direct uploaded file or benchmark sample selection
        if file and file.filename != '':
            if not allowed_file(file.filename):
                flash("Unsupported file format. Please upload JPG, JPEG, PNG, or WEBP.", "danger")
                return redirect(request.url)
            ext = file.filename.rsplit('.', 1)[1].lower()
            unique_name = f"leaf_{uuid.uuid4().hex[:12]}.{ext}"
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_name)
            file.save(save_path)
        elif sample_name:
            import shutil
            sample_src = os.path.join(app.root_path, 'static', 'img', 'samples', sample_name)
            if not os.path.exists(sample_src):
                flash("Specified sample specimen not found.", "danger")
                return redirect(request.url)
            unique_name = f"leaf_sample_{uuid.uuid4().hex[:8]}.jpg"
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_name)
            shutil.copyfile(sample_src, save_path)
        else:
            flash("No leaf image provided. Please upload a photo or select a test specimen.", "danger")
            return redirect(request.url)

        # Execute ML prediction pipeline
        result = predict_leaf_disease(save_path)

        if result.get('error'):
            flash(f"Inference error: {result['error']}", "danger")
            return redirect(request.url)

        # Save to SQLite Database
        pred_id = save_prediction(
            user_id=user_id,
            filename=unique_name,
            filepath=save_path,
            predicted_class=result['predicted_class'],
            confidence=result['confidence'],
            is_healthy=result['is_healthy'],
            is_demo=result['is_demo'],
            notes=result.get('mode', '')
        )

        uploaded_img_url = url_for('uploaded_file', filename=unique_name)
        flash(f"Analysis complete: {result['predicted_class']} ({result['confidence_pct']} confidence)", "success")
        return render_template('detect.html', result=result, uploaded_image_url=uploaded_img_url)

    return render_template('detect.html', result=None)

@app.route('/history')
@login_required
def history():
    """Historical records view."""
    user_id = session['user_id']
    predictions = get_user_predictions(user_id, limit=100)
    return render_template('history.html', predictions=predictions)

@app.route('/history/delete/<int:item_id>', methods=['POST'])
@login_required
def delete_history_item(item_id):
    """Delete a single prediction record."""
    user_id = session['user_id']
    success = delete_prediction_by_id(item_id, user_id)
    if success:
        flash("Record deleted.", "info")
    else:
        flash("Record could not be removed or unauthorized.", "danger")
    return redirect(url_for('history'))

@app.route('/history/clear', methods=['POST'])
@login_required
def clear_history():
    """Clear all records for the active user."""
    user_id = session['user_id']
    count = clear_user_predictions(user_id)
    flash(f"Successfully deleted {count} diagnostic history records.", "info")
    return redirect(url_for('history'))

@app.route('/diseases')
def disease_info():
    """Public searchable and filterable disease catalog."""
    filter_cat = request.args.get('filter', 'all').strip().lower()
    search_query = request.args.get('q', '').strip().lower()

    # Get categories for the chosen group filter
    categories = get_categories_by_group(filter_cat)

    # Apply client-side-style server search filter
    if search_query:
        categories = [
            c for c in categories
            if search_query in c['name'].lower()
            or search_query in c.get('description', '').lower()
            or search_query in c.get('scientific_name', '').lower()
            or search_query in ' '.join(c.get('symptoms', [])).lower()
        ]

    all_categories = get_all_categories()
    ml_supported = get_ml_supported_categories()
    reference_only = get_reference_only_categories()

    groups = [
        ('all', 'All Categories'),
        ('healthy', 'Healthy'),
        ('fungal', 'Fungal'),
        ('bacterial', 'Bacterial'),
        ('viral', 'Viral'),
        ('pest_related', 'Pest Damage'),
        ('physiological', 'Physiological'),
        ('uncertain', 'Unknown / Uncertain'),
    ]

    return render_template(
        'disease_info.html',
        categories=categories,
        groups=groups,
        active_filter=filter_cat,
        search_query=search_query,
        total_count=len(all_categories),
        ml_supported_count=len(ml_supported),
        reference_only_count=len(reference_only),
        ml_supported_ids=[c['id'] for c in ml_supported],
    )


@app.route('/diseases/<disease_id>')
def disease_detail(disease_id):
    """Per-disease detail page with full agronomic profile."""
    info = DISEASE_CATALOG.get(disease_id)
    if not info:
        abort(404)
    return render_template('disease_detail.html', disease=info)

@app.route('/about')
def about():
    """Technical B.Tech CSE project overview."""
    return render_template('about.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """Serve uploaded specimen photos safely."""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/api/status')
def api_status():
    """System health & model status check."""
    status = get_model_status()
    return jsonify(status)

# ----------------- Error Handlers -----------------

@app.errorhandler(404)
def not_found_error(error):
    return render_template('error.html', error_title="Page Not Found", error_message="The requested URL was not found on this server."), 404

@app.errorhandler(413)
def request_entity_too_large(error):
    flash("The uploaded file exceeds the 8 MB maximum size limit.", "danger")
    return redirect(url_for('detect'))

@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html', error_title="Internal Server Error", error_message="An unexpected server error occurred. Please try again."), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    try:
        app.run(host='0.0.0.0', port=port, debug=Config.DEBUG)
    except OSError as e:
        if '10048' in str(e) or 'address already in use' in str(e).lower():
            fallback_port = 5001
            print(f"[PlantCare AI] Port {port} is in use. Falling back to http://127.0.0.1:{fallback_port}")
            app.run(host='0.0.0.0', port=fallback_port, debug=Config.DEBUG)
        else:
            raise
