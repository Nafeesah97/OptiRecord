#!/usr/bin/python3
"""
importing necessary libraries
sign in
"""
import uuid
from flask import Flask, render_template, url_for, flash, redirect, request, abort
from flask_login import current_user
from models import storage
from models.form import RegistrationForm
from models.user import User
from flask_bcrypt import Bcrypt
from models import storage



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


@app.route('/sign_up', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = Bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        storage.add(user)
        storage.save()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('sign_in'))
    return render_template('sign_up.html', form=form)

if __name__ == "__main__":
    """ Main Function """
    app.run(host='52.91.202.165', port=5005, debug=True)
