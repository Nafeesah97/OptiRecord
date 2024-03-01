#!/usr/bin/python3
"""
importing necessary libraries
sign in
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask import render_template, url_for, flash, redirect, request, abort
from flask_login import current_user, login_user
import sqlite3


app = Flask(__name__, template_folder="templates")
app.url_map.strict_slashes = False
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba290'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
Base = db.Model

@login_manager.user_loader
def load_user(user_id):
    from user import User
    return User.query.get(int(user_id))


with app.app_context():
    db.create_all()

@app.teardown_appcontext
def teardown_db(exception):
    """
    after each request, this method calls .close() (i.e. .remove()) on
    the current SQLAlchemy Session
    """
    db.session.close()


@app.route("/home", methods=['GET'])

def home():
    from drug import Drug
    from patient import Patient
    from procedure import Procedure
    from frame import Frame
    query = request.args.get('search', '')
    filter_by = request.args.get('search_table', '')
    page = request.args.get('page', 1, type=int)

    if filter_by == 'patient':
        patients = Patient.query.filter((Patient.first_name.like(f'%{query}%')) | (Patient.last_name.like(f'%{query}%')) | (Patient.id.like(f'%{query}%'))).paginate(page=page, per_page=10)
        return render_template('home.html', title='home', patients=patients, query=query, filter_by=filter_by)
    elif filter_by == 'drug':
        drugs = Drug.query.filter((Drug.name.like(f'%{query}%')) | (Drug.id.like(f'%{query}%'))).paginate(page=page, per_page=10)
        return render_template('home.html', title='home', drugs=drugs, query=query, filter_by=filter_by)
    elif filter_by == 'frame':
        frames = Frame.query.filter((Frame.name.like(f'%{query}%')) | (Frame.id.like(f'%{query}%'))).paginate(page=page, per_page=10)
        return render_template('home.html', title='home', frames=frames, query=query, filter_by=filter_by)
    elif filter_by == 'procedure':
        procedures = Procedure.query.filter((Procedure.test_type.like(f'%{query}%')) | (Procedure.id.like(f'%{query}%'))).paginate(page=page, per_page=10)
        return render_template('home.html', title='home', procedures=procedures, query=query, filter_by=filter_by)
    else:
        patients = Patient.query.filter((Patient.first_name.like(f'%{query}%')) | (Patient.last_name.like(f'%{query}%')) | (Patient.id.like(f'%{query}%'))).paginate(page=page, per_page=10)
        drugs = Drug.query.filter((Drug.name.like(f'%{query}%')) | (Drug.id.like(f'%{query}%'))).paginate(page=page, per_page=10)
        frames = Frame.query.filter((Frame.name.like(f'%{query}%')) | (Frame.id.like(f'%{query}%'))).paginate(page=page, per_page=10)
        procedures = Procedure.query.filter((Procedure.test_type.like(f'%{query}%')) | (Procedure.id.like(f'%{query}%'))).paginate(page=page, per_page=10)
        
        return render_template('home.html', title='home', patients=patients, drugs=drugs, frames=frames, procedures=procedures, query=query, filter_by=filter_by)


@app.route('/sign_in', methods=['GET', 'POST'], endpoint='signin_page')
def login():
    from form import LoginForm
    from user import User
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('sign_in.html', title='Login', form=form)

@app.route('/sign_up', methods=['GET', 'POST'])
def register():
    from form import RegistrationForm
    from user import User
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('sign_in'))
    return render_template('sign_up.html', title='Register', form=form)

if __name__ == "__main__":
    app.run(debug=True)