#!/usr/bin/python3
"""
importing necessary libraries
for the optician table
"""
from patient import PhoneNumberType
import re
from routes import db


class Optician(db.Model):
    """
    To create the staffs table
    """
    __tablename__ = 'opticians'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    sex = db.Column(db.Enum('F', 'M'), nullable=False)
    DOB = db.Column(db.Date, nullable=False)
    Email = db.Column(db.String(30), nullable=False)
    contact_no = db.Column(PhoneNumberType, nullable=False)
    Address = db.Column(db.String(128), nullable=False)
    consult = db.relationship("Consultation", backref="optician")


    def is_valid_email(email):
        """To validate email"""
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None