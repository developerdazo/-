from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import PasswordField, SubmitField, StringField, DateField
from wtforms.fields.html5 import EmailField 
from wtforms.validators import DataRequired, Email, Length


class signupform(FlaskForm):
    email = EmailField('メールアドレス', validators=[DataRequired(), Email()])
    password = PasswordField('パスワード', validators=[DataRequired(), Length(max=100)])
    name = StringField('名前', validators=[DataRequired(), Length(max=1000)])
    loginid = StringField('id', validators=[DataRequired(), Length(max=1000)])
    birthday = DateField('生年月日', validators=[DataRequired()])
    submit = SubmitField('登録')