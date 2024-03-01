#!/usr/bin/python3
"""
importing necessary libraries
for the patients table
"""
import phonenumbers
import re
from routes import db


class PhoneNumberType(db.TypeDecorator):
    impl = db.String(20)

    def process_bind_param(self, value, dialect):
        # Validate and format the phone number before storing it in the database
        if value is not None:
            try:
                phone_number = phonenumbers.parse(value, None)  # No default region
            except phonenumbers.phonenumberutil.NumberParseException as e:
                raise ValueError("Invalid phone number") from e
            if not phonenumbers.is_valid_number(phone_number):
                raise ValueError("Invalid phone number")
            return phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.E164)
        return None


    def process_result_value(self, value, dialect):
        # Return the stored phone number as is
        return value

class Patient(db.Model):
    """
    To create the patients table
    """
    __tablename__ = 'patients'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    sex = db.Column(db.Enum('F', 'M'), nullable=False)
    DOB = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(30))
    contact_no = db.Column(PhoneNumberType, nullable=False)
    address = db.Column(db.String(128), nullable=False)
    """consult = db.relationship("Consultation", backref="patient")
    bill = db.relationship("Bill", backref="patient")"""

    def is_valid_email(email):
        """To validate email"""
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None