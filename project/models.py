from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True,nullable=False)# メールアドレス（最大１００文字、ユニーク、必須項目）
    password = db.Column(db.String(100),nullable=False)#パス(最大100文字、必須)
    name = db.Column(db.String(1000),nullable=False)#名前(1000文字以内、必須)
    loginid = db.Column(db.String(1000),nullable=False)#id(パス忘れたよう、1000文字以内、必須)
    birthday = db.Column(db.DateTime,nullable=False)#誕生日(日付、必須)
    phonenumber = db.Column(db.String(15),nullable=False,unique=True)#電話(15文字以内、必須、ユニーク)