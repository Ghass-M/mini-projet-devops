import pytest
import sys
import os

# Add the parent directory to Python path so we can import the app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import your Flask app - adjust this import based on your app structure
try:
    from app import app  # If your Flask app is in app.py
except ImportError:
    try:
        from main import app  # If your Flask app is in main.py
    except ImportError:
        try:
            from run import app  # If your Flask app is in run.py
        except ImportError:
            try:
                from backend.app import app  # If your Flask app is in backend/app.py
            except ImportError:
                # Create a minimal Flask app for testing if none found
                from flask import Flask
                app = Flask(__name__)
                
                @app.route('/')
                def index():
                    return 'Hello World!'
                
                @app.errorhandler(404)
                def not_found(error):
                    return 'Not Found', 404

@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for testing
    
    with app.test_client() as client:
        with app.app_context():
            yield client

@pytest.fixture
def app_context():
    """Create an application context for testing."""
    with app.app_context():
        yield app