from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from .models import User

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    loginid = request.form.get('loginid')
    birthday = request.form.get('birthday')
    phonenumber = request.form.get('phonenumber')


    print(email,name,password,loginid,birthday,phonenumber)
    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    # if user: # if a user is found, we want to redirect back to signup page so user can try again
    #     return redirect(url_for('auth.signup'))

    # # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    # new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # # add the new user to the database
    # db.session.add(new_user)
    # db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/logout')
def logout():
    return 'Logout'
























@auth.route('/signup')
def signup():
    return render_template('signup.html')