import os

class Config:
    """Configuration settings for the Medical Insurance Prediction application."""
    
    # Base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Model and data paths
    MODEL_FILE_PATH = os.path.join(BASE_DIR, 'project_app', 'linear_regression.pkl')
    JSON_FILE_PATH = os.path.join(BASE_DIR, 'project_app', 'label_enc_data.json')
    
    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here')
    DEBUG = True
    
    # API settings
    API_TITLE = "Medical Insurance Prediction API"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.2"
    
    # Input validation
    MIN_AGE = 18
    MAX_AGE = 100
    MIN_BMI = 10
    MAX_BMI = 50
    MAX_CHILDREN = 5 