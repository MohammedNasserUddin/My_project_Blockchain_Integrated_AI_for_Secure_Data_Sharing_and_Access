from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

# ----------------------
# User Model
# ----------------------
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"


# ----------------------
# Analysis History Model
# ----------------------
class AnalysisHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    input_type = db.Column(db.String(50))       # Text / File
    content = db.Column(db.Text)                # User input
    risk_level = db.Column(db.String(50))       # Low / Medium / High / Critical
    hash_value = db.Column(db.String(256))      # Blockchain hash

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Analysis {self.id} - {self.risk_level}>"