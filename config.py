import os
from pathlib import Path
from dotenv import load_dotenv

# Suppress verbose TensorFlow & oneDNN logging
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# Load environment variables from .env if present
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent

class Config:
    """Application configuration settings."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'plantcare-super-secret-key-change-in-production-2025')
    
    # Database
    DATABASE_PATH = os.environ.get('DATABASE_PATH', str(BASE_DIR / 'instance' / 'plantcare.db'))
    
    # Uploads
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', str(BASE_DIR / 'static' / 'uploads'))
    MAX_CONTENT_LENGTH = int(os.environ.get('MAX_CONTENT_LENGTH', 8 * 1024 * 1024))  # 8 MB
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp'}
    
    # Model
    MODEL_PATH = os.environ.get('MODEL_PATH', str(BASE_DIR / 'ml' / 'models' / 'plantcare_mobilenetv2.keras'))
    ENABLE_REAL_MODEL = os.environ.get('ENABLE_REAL_MODEL', 'False').lower() in ('true', '1', 't')
    
    # Firebase Cloud configuration (optional)
    FIREBASE_ENABLED = os.environ.get('FIREBASE_ENABLED', 'False').lower() in ('true', '1', 't')
    FIREBASE_CREDENTIALS = os.environ.get('FIREBASE_CREDENTIALS', '')
    FIREBASE_STORAGE_BUCKET = os.environ.get('FIREBASE_STORAGE_BUCKET', '')
    
    # Application Mode
    DEBUG = os.environ.get('FLASK_DEBUG', 'True').lower() in ('true', '1', 't')
