#!/usr/bin/python3
"""
importing necessary libraries
for the user table
"""
from patient import PhoneNumberType
from routes import db
import re
from flask_login import UserMixin


class User(db.Model, UserMixin):
    """
    To create the staffs table
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.png')
    password = db.Column(db.String(60), nullable=False)

    def is_valid_email(email):
        """To validate email"""
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"