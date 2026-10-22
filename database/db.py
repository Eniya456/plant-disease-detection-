import sqlite3
import os
from pathlib import Path
from werkzeug.security import generate_password_hash, check_password_hash

def get_db_path():
    try:
        from flask import current_app
        if current_app and 'DATABASE_PATH' in current_app.config:
            db_path = Path(current_app.config['DATABASE_PATH'])
            db_path.parent.mkdir(parents=True, exist_ok=True)
            return str(db_path)
    except Exception:
        pass
    from config import Config
    db_path = Path(Config.DATABASE_PATH)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    return str(db_path)

def get_connection():
    """Returns a SQLite connection with Row factory."""
    conn = sqlite3.connect(get_db_path())
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def init_db():
    """Initializes tables and seeds default demo account if needed."""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Create Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            full_name TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Create Predictions table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            filename TEXT NOT NULL,
            filepath TEXT NOT NULL,
            predicted_class TEXT NOT NULL,
            confidence REAL NOT NULL,
            is_healthy INTEGER DEFAULT 0,
            is_demo INTEGER DEFAULT 0,
            notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        )
    """)
    
    conn.commit()
    
    # Check if demo account exists
    cursor.execute("SELECT id FROM users WHERE email = ?", ('demo@plantcare.ai',))
    demo_user = cursor.fetchone()
    if not demo_user:
        hashed_pw = generate_password_hash('Demo@1234')
        cursor.execute(
            "INSERT INTO users (username, email, password_hash, full_name) VALUES (?, ?, ?, ?)",
            ('demo_user', 'demo@plantcare.ai', hashed_pw, 'Demo Agronomist')
        )
        conn.commit()
        demo_id = cursor.lastrowid
        
        # Seed 3 initial demonstration scans for immediate dashboard visualization
        cursor.execute("""
            INSERT INTO predictions (user_id, filename, filepath, predicted_class, confidence, is_healthy, is_demo, notes)
            VALUES 
            (?, 'early_blight_sample.jpg', 'static/img/samples/early_blight_leaf.jpg', 'Early blight', 0.948, 0, 1, 'Initial field scouting benchmark'),
            (?, 'healthy_sample.jpg', 'static/img/samples/healthy_leaf.jpg', 'Healthy', 0.923, 1, 1, 'Control crop greenhouse specimen'),
            (?, 'late_blight_sample.jpg', 'static/img/samples/late_blight_leaf.jpg', 'Late blight', 0.884, 0, 1, 'High humidity perimeter plot')
        """, (demo_id, demo_id, demo_id))
        conn.commit()
    
    conn.close()

# ----------------- User Authentication Helpers -----------------

def create_user(username, email, password, full_name=""):
    """Register a new user with hashed password."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        pw_hash = generate_password_hash(password)
        cursor.execute(
            "INSERT INTO users (username, email, password_hash, full_name) VALUES (?, ?, ?, ?)",
            (username.strip(), email.strip().lower(), pw_hash, full_name.strip())
        )
        conn.commit()
        user_id = cursor.lastrowid
        return {"success": True, "user_id": user_id}
    except sqlite3.IntegrityError as e:
        error_msg = str(e).lower()
        if 'username' in error_msg:
            return {"success": False, "error": "Username is already registered."}
        elif 'email' in error_msg:
            return {"success": False, "error": "Email address is already registered."}
        return {"success": False, "error": "Account could not be created. Please check inputs."}
    finally:
        conn.close()

def get_user_by_email_or_username(identifier):
    """Fetch user by either username or email."""
    conn = get_connection()
    cursor = conn.cursor()
    identifier = identifier.strip().lower()
    cursor.execute(
        "SELECT * FROM users WHERE LOWER(email) = ? OR LOWER(username) = ?",
        (identifier, identifier)
    )
    user = cursor.fetchone()
    conn.close()
    return dict(user) if user else None

def get_user_by_id(user_id):
    """Fetch user by primary key ID."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, email, full_name, created_at FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    return dict(user) if user else None

def authenticate_user(identifier, password):
    """Authenticate credentials; returns user dict or None."""
    user = get_user_by_email_or_username(identifier)
    if user and check_password_hash(user['password_hash'], password):
        # Don't pass password hash around
        user_clean = {k: v for k, v in user.items() if k != 'password_hash'}
        return user_clean
    return None

# ----------------- Prediction History Helpers -----------------

def save_prediction(user_id, filename, filepath, predicted_class, confidence, is_healthy=False, is_demo=False, notes=""):
    """Save a prediction result to SQLite database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO predictions (user_id, filename, filepath, predicted_class, confidence, is_healthy, is_demo, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        user_id,
        filename,
        filepath,
        predicted_class,
        round(float(confidence), 4),
        1 if is_healthy else 0,
        1 if is_demo else 0,
        notes
    ))
    conn.commit()
    pred_id = cursor.lastrowid
    conn.close()
    return pred_id

def get_user_predictions(user_id, limit=50):
    """Retrieve historical predictions for a specific user."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM predictions 
        WHERE user_id = ? 
        ORDER BY created_at DESC 
        LIMIT ?
    """, (user_id, limit))
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_prediction_by_id(prediction_id, user_id):
    """Retrieve a single prediction ensuring ownership."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM predictions 
        WHERE id = ? AND user_id = ?
    """, (prediction_id, user_id))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

def get_user_stats(user_id):
    """Compute dashboard statistics for a given user."""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Total count
    cursor.execute("SELECT COUNT(*) FROM predictions WHERE user_id = ?", (user_id,))
    total = cursor.fetchone()[0]
    
    # Healthy count
    cursor.execute("SELECT COUNT(*) FROM predictions WHERE user_id = ? AND is_healthy = 1", (user_id,))
    healthy = cursor.fetchone()[0]
    
    # Diseased count
    diseased = total - healthy
    
    # Average confidence
    cursor.execute("SELECT AVG(confidence) FROM predictions WHERE user_id = ?", (user_id,))
    avg_conf = cursor.fetchone()[0]
    avg_conf = round(avg_conf * 100, 1) if avg_conf else 0.0
    
    # Category breakdown for charts
    cursor.execute("""
        SELECT predicted_class, COUNT(*) as count 
        FROM predictions 
        WHERE user_id = ? 
        GROUP BY predicted_class
        ORDER BY count DESC
    """, (user_id,))
    category_counts = [dict(row) for row in cursor.fetchall()]
    
    conn.close()
    return {
        "total_predictions": total,
        "healthy_count": healthy,
        "diseased_count": diseased,
        "avg_confidence": avg_conf,
        "category_counts": category_counts
    }

def clear_user_predictions(user_id):
    """Clear all prediction records for the current user."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM predictions WHERE user_id = ?", (user_id,))
    deleted = cursor.rowcount
    conn.commit()
    conn.close()
    return deleted

def delete_prediction_by_id(prediction_id, user_id):
    """Delete a single prediction record."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM predictions WHERE id = ? AND user_id = ?", (prediction_id, user_id))
    deleted = cursor.rowcount
    conn.commit()
    conn.close()
    return deleted > 0
