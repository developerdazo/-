#from project.Forms.LoginForm import LoginForm
from project.Forms.LoginForm import LoginForm
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .models import User
import datetime
from flask_login import login_user, logout_user, login_required






auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


@auth.route('/login', methods=['POST'])
def login_post():
    
    form = LoginForm()
    if form.validate_on_submit():
        print(form.email, form.password)
     
        email=form.email.data
        password=form.password.data
        user = User.query.filter_by(email=email).first()
    

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
        login_user(user, remember=True)
        return redirect(url_for('main.profile'))
    flash("不正アクセス禁止法")
    return redirect(url_for('auth.login'))

@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    loginid = request.form.get('loginid')
    birthday = datetime.datetime.strptime(request.form.get('birthday'), '%Y-%m-%d')
    phonenumber = request.form.get('phonenumber')


    print(email,name,password,loginid,birthday,phonenumber)
    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        return redirect(url_for('auth.login'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'), loginid=loginid, birthday=birthday, phonenumber=phonenumber)

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))
    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))
























@auth.route('/signup')
def signup():
    return render_template('signup.html')