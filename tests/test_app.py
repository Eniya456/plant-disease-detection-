import os
import io
import uuid
import unittest
from app import app
from database.db import get_connection, init_db

class PlantCareTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.test_db = os.path.abspath(f"instance/test_{uuid.uuid4().hex[:8]}.db")
        app.config['DATABASE_PATH'] = self.test_db
        app.config['SECRET_KEY'] = 'test-secret-key'
        
        self.app = app.test_client()
        with app.app_context():
            init_db()

    def tearDown(self):
        if hasattr(self, 'test_db') and os.path.exists(self.test_db):
            try:
                os.remove(self.test_db)
            except Exception:
                pass

    def test_public_pages(self):
        """Verify public endpoints return 200 OK."""
        for path in ['/', '/diseases', '/about', '/login', '/register', '/api/status']:
            response = self.app.get(path)
            self.assertEqual(response.status_code, 200, f"Failed on path {path}")

    def test_demo_user_seeded(self):
        """Verify default demo user exists and can authenticate."""
        response = self.app.post('/login', data={
            'identifier': 'demo@plantcare.ai',
            'password': 'Demo@1234'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Dashboard', response.data)

    def test_user_registration_and_login(self):
        """Test registration workflow, password validation, and subsequent login."""
        # Register new user
        reg_resp = self.app.post('/register', data={
            'full_name': 'Test Botanist',
            'username': 'botanist_test',
            'email': 'botanist@test.org',
            'password': 'SecretPassword123',
            'confirm_password': 'SecretPassword123'
        }, follow_redirects=True)
        self.assertEqual(reg_resp.status_code, 200)
        self.assertIn(b'Account registered successfully', reg_resp.data)

        # Login with newly created user
        login_resp = self.app.post('/login', data={
            'identifier': 'botanist_test',
            'password': 'SecretPassword123'
        }, follow_redirects=True)
        self.assertEqual(login_resp.status_code, 200)
        self.assertIn(b'Welcome back, Test Botanist!', login_resp.data)

    def test_detect_and_history_workflow(self):
        """Test full scan workflow: login, leaf image upload, prediction, and history lookup."""
        # 1. Login as demo user
        self.app.post('/login', data={
            'identifier': 'demo@plantcare.ai',
            'password': 'Demo@1234'
        }, follow_redirects=True)

        # 2. Upload test leaf image
        with open('static/img/samples/early_blight_leaf.jpg', 'rb') as f:
            img_bytes = f.read()

        upload_data = {
            'leaf_image': (io.BytesIO(img_bytes), 'test_early_blight.jpg')
        }

        detect_resp = self.app.post('/detect', data=upload_data, content_type='multipart/form-data', follow_redirects=True)
        self.assertEqual(detect_resp.status_code, 200)
        self.assertIn(b'Early blight', detect_resp.data)
        self.assertIn(b'Alternaria solani', detect_resp.data)

        # 3. Check Dashboard statistics
        dash_resp = self.app.get('/dashboard')
        self.assertEqual(dash_resp.status_code, 200)
        self.assertIn(b'Total Scans', dash_resp.data)

        # 4. Check History table
        hist_resp = self.app.get('/history')
        self.assertEqual(hist_resp.status_code, 200)
        self.assertIn(b'Early blight', hist_resp.data)

        # 5. Clear history
        clear_resp = self.app.post('/history/clear', follow_redirects=True)
        self.assertEqual(clear_resp.status_code, 200)
        self.assertIn(b'Successfully deleted', clear_resp.data)

if __name__ == '__main__':
    unittest.main()
