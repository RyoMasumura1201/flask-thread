from flask_sqlalchemy import SQLAlchemy
from controllers.controller import app

db = SQLAlchemy(app)

class Task(db.Model):
    name = db.Column(db.String(64), primary_key=True)
    status = db.Column(db.String(64))