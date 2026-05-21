import os

class Config:
    # Secret key for signing cookies and session data
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-very-secret-permanent-key'
    
    # Database configuration (Defaults to a local SQLite file)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
    
    # Disable track modifications to save resources
    SQLALCHEMY_TRACK_MODIFICATIONS = False