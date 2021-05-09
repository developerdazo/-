from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True,nullable=False)
    password = db.Column(db.String(100),nullable=False)
    name = db.Column(db.String(1000),nullable=False)
    loginid = db.Column(db.String(1000),nullable=False)
    birthday = db.Column(db.DateTime,nullable=False)
    phonenumber = db.Column(db.String(15),nullable=False,unique=True)