#!/usr/bin/python3
"""
importing necessary libraries
sign in
"""
import uuid
from flask import Flask, render_template, url_for, flash, redirect, request, abort
from flask_login import current_user, login_user
from models import storage
from models.form import LoginForm
from models.user import User
from flask_bcrypt import Bcrypt



# flask setup
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'

@app.teardown_appcontext
def teardown_db(exception):
    """
    after each request, this method calls .close() (i.e. .remove()) on
    the current SQLAlchemy Session
    """
    storage.close()


@app.route('/sign_in', methods=['GET', 'POST'])
def login():
    """
    handles request to log in
    """
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and Bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('sign_in.html', form=form)
