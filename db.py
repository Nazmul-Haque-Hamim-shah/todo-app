from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Tasks(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    text=db.Column(db.String(100),nullable=False)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(200),unique=True,nullable=False)
    email=db.Column(db.String(200),unique=True,nullable=False)
    password=db.Column(db.String(500),nullable=False)
