# PlantCare AI — Plant Leaf Disease Classification System Using Machine Learning and Cloud Computing

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.x-green.svg)](https://palletsprojects.com/p/flask/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-Keras-orange.svg)](https://tensorflow.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple.svg)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-Academic_Capstone-lightgrey.svg)]()

> **B.Tech Computer Science & Engineering (CSE) Capstone Project**  
> An end-to-end, full-stack intelligent crop pathology diagnostic platform designed to detect foliar diseases in tomato crops using Convolutional Neural Networks (CNNs), responsive Web & Mobile interfaces, and cloud-ready infrastructure.

---

## 📌 1. Project Overview & Objectives

Foliar crop diseases can decimate up to 40% of agricultural harvests if undetected in their initial phases. Traditional field diagnosis requires specialized agronomists, which is cost-prohibitive for smallholder farmers. 

**PlantCare AI** provides:
- **Instant Leaf Disease Classification:** Sub-second diagnostic feedback on uploaded leaf photographs.
- **5 Supported Foliar Categories:**
  1. **Healthy Tomato Leaf** (*Normal tissue & chlorophyll*)
  2. **Early Blight** (*Alternaria solani*)
  3. **Late Blight** (*Phytophthora infestans*)
  4. **Leaf Mold** (*Passalora fulva*)
  5. **Septoria Leaf Spot** (*Septoria lycopersici*)
- **Complete Agronomic Action Plans:** Symptom identification, pathogen etiology, cultural preventative practices, and organic/chemical control measures.
- **Analytics & History Tracking:** User-specific dashboard with health ratios, distribution charts, and persistent scan logs.
- **Zero-Friction Evaluation:** Built-in demo accounts and pre-packaged test specimens for immediate assessment without camera hardware or external API keys.

---

## 🏗️ 2. System Architecture & Pillars

PlantCare AI unites three foundational pillars of modern Computer Science:

```
+-----------------------------------------------------------------------------------+
|                        1. Web & Mobile Computing (WMC)                            |
|  - Responsive Bootstrap 5.3 UI (Mobile, Tablet, Desktop)                         |
|  - Drag-and-Drop Image Ingestion with Instant Client-Side Preview & Validation    |
|  - Low-latency asynchronous JSON / Multipart REST APIs                            |
+-----------------------------------------------------------------------------------+
                                        | (Leaf Image Upload)
                                        v
+-----------------------------------------------------------------------------------+
|                     2. Machine Learning & Computer Vision                         |
|  - Preprocessing Matrix: 224x224 RGB standardization & [-1, 1] normalization      |
|  - Deep Learning CNN (MobileNetV2 Inverted Residual Backbone)                     |
|  - Softmax Classification Head over 5 discrete foliar disease categories          |
|  - Modular Fallback: Transparent Botanical Color & Necrosis Heuristic Engine     |
+-----------------------------------------------------------------------------------+
                                        | (Classification & Metadata)
                                        v
+-----------------------------------------------------------------------------------+
|                     3. Cloud Computing & Data Persistence                         |
|  - Default Local Database: Zero-configuration SQLite (`instance/plantcare.db`)   |
|  - Cloud Deployment Ready: Stateless 12-factor architecture with `Procfile`      |
|  - Cloud Storage Extensibility: Documented hooks for Firebase Storage & Firestore|
+-----------------------------------------------------------------------------------+
```

---

## 💻 3. Technology Stack

| Layer | Technologies |
| :--- | :--- |
| **Frontend** | HTML5, CSS3 (Custom Agricultural Green Palette), JavaScript (ES6+), Bootstrap 5.3, Bootstrap Icons, Chart.js |
| **Backend** | Python 3.x, Flask, Werkzeug Security (PBKDF2 Password Hashing), Jinja2 |
| **Machine Learning** | TensorFlow / Keras, NumPy, Pillow (PIL), MobileNetV2 architecture |
| **Database** | SQLite (Default persistent local DB with foreign key constraints) |
| **Cloud / DevOps** | Gunicorn WSGI, Environment-variable config (`python-dotenv`), Procfile |

---

## 📂 4. Project Directory Structure

```text
plant_detection/
├── app.py                     # Main Flask application, routes, authentication & error handling
├── config.py                  # Environment-driven application configuration
├── requirements.txt           # Python dependencies
├── Procfile                   # Cloud PaaS production execution definition
├── .env.example               # Environment variable templates
├── .gitignore                 # Excludes cache, secrets, and SQLite instances
├── README.md                  # Project documentation & setup instructions
│
├── ml/
│   ├── __init__.py
│   ├── predictor.py           # Preprocessing, CNN model inference & heuristic analyzer
│   └── disease_catalog.py     # Comprehensive botanical pathogen knowledge base
│
├── database/
│   ├── __init__.py
│   └── db.py                  # SQLite schema definitions, user auth & history CRUD
│
├── static/
│   ├── css/
│   │   └── style.css          # Modern agricultural UI theme
│   ├── js/
│   │   └── main.js            # Drag-and-drop, image preview & async feedback
│   ├── img/
│   │   └── samples/           # Built-in sample leaf specimens for instant testing
│   └── uploads/               # Isolated storage for uploaded user scans
│
├── templates/
│   ├── base.html              # Shell layout, sidebar navigation, topbar & footer
│   ├── index.html             # Landing page, feature overview & how-it-works
│   ├── login.html             # Secure login with 1-click Demo Account button
│   ├── register.html          # Registration form with input validation
│   ├── dashboard.html         # Analytics dashboard, statistics & Chart.js widgets
│   ├── detect.html            # Drag-and-drop scanner, results card & advice tabs
│   ├── history.html           # Historical scan repository, search filter & deletion
│   ├── disease_info.html      # 5-class foliar pathology reference guide
│   └── about.html             # Academic B.Tech CSE thesis overview & architecture
│
└── instance/
    └── plantcare.db           # SQLite database (auto-created on first run)
```

---

## ⚡ 5. Quick Start & Execution Guide

### Prerequisites
- Python 3.10, 3.11, 3.12, 3.13, or 3.14
- `pip` package manager

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Initialize Database (Automatic)
The database and tables are created automatically on the first start of `app.py`. A pre-seeded demo user is also created:
- **Demo Email:** `demo@plantcare.ai`
- **Demo Username:** `demo_user`
- **Demo Password:** `Demo@1234`

### Step 3: Run the Application
```bash
python app.py
```

Open your browser and navigate to:
```
http://127.0.0.1:5000
```

---

## 🧪 6. Testing the Application

1. **Sign In:**
   - Go to `/login` and click **"Use Demo Account"** for 1-click login, or create a new user on `/register`.
2. **Dashboard (`/dashboard`):**
   - View your total scans, healthy vs diseased breakdown, and live Chart.js visualization.
3. **Run Leaf Scans (`/detect`):**
   - Either drag and drop any tomato leaf image (`.jpg`, `.jpeg`, `.png`, `.webp`) or click any of the **5 built-in benchmark specimens** on the left panel:
     - `Healthy Leaf`
     - `Early Blight`
     - `Late Blight`
     - `Leaf Mold`
     - `Septoria Leaf Spot`
   - Observe the progress animation, classification badge, confidence meter, class probabilities, symptoms, and agronomic prevention advice.
4. **Inspect History (`/history`):**
   - Search previous scans, open detailed reports, or clear history.

---

## ☁️ 7. Cloud Deployment & Firebase Integration

### Cloud PaaS Deployment (Render / Heroku / Railway)
1. Fork or push this repository to GitHub.
2. Link the repository to your cloud provider (e.g. [Render](https://render.com) or [Heroku](https://heroku.com)).
3. Configure Environment Variables:
   - `SECRET_KEY`: A strong random string (e.g., `openssl rand -hex 24`).
   - `FLASK_DEBUG`: `False`.
   - `PORT`: Provided dynamically by cloud host.
4. The included `Procfile` executes:
   ```bash
   web: gunicorn app:app --bind 0.0.0.0:$PORT
   ```

### Optional Firebase Integration
To link Google Firebase Cloud Storage and Firestore:
1. Create a Firebase project in the [Firebase Console](https://console.firebase.google.com/).
2. Enable **Firestore Database** and **Cloud Storage**.
3. Generate a private service account key JSON file from **Project Settings > Service Accounts**.
4. Set the following environment variables in your `.env` or cloud dashboard:
   ```bash
   FIREBASE_ENABLED=True
   FIREBASE_CREDENTIALS=path/to/firebase_service_account.json
   FIREBASE_STORAGE_BUCKET=your-project-id.appspot.com
   ```
5. Install the Firebase Admin SDK if enabled:
   ```bash
   pip install firebase-admin
   ```

---

## 🔒 8. Security & Reliability Implementations

- **Password Hashing:** Passwords are never stored in plaintext. They are hashed using Werkzeug PBKDF2 with SHA-256 and salted.
- **Session Management:** Secure HTTP session cookies protect authenticated views (`@login_required`).
- **Filename Sanitization:** All incoming files are sanitized via `werkzeug.utils.secure_filename` and assigned cryptographic UUID prefixes (`leaf_<uuid>.ext`) to eliminate path traversal vulnerabilities.
- **Data Isolation:** SQL queries are scoped to the active `session['user_id']`, preventing cross-tenant data leakage.
- **Size Limitation:** Payloads exceeding 8 MB are rejected gracefully with a 413 HTTP status code.

---

## ⚠️ 9. Academic Disclaimer

PlantCare AI was developed as an educational capstone project. While the underlying Convolutional Neural Network demonstrates strong diagnostic benchmarks on standardized foliar datasets, field conditions (e.g., uneven sunlight, multiple concurrent blights, insect damage) can alter leaf morphology. Predictions should be corroborated by agricultural extension professionals before deploying chemical pest management solutions.
