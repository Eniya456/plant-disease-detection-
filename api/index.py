import sys
import os

# Add the project root to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# Ensure /tmp directories exist for Vercel serverless
os.makedirs('/tmp/uploads', exist_ok=True)

from app import app

# Vercel serverless handler
app = app
