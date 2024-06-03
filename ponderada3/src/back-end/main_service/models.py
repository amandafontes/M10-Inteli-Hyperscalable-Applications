from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MainData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    attribute = db.Column(db.String(120), nullable=False)
