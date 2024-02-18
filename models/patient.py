#!/usr/bin/python3
"""
importing necessary libraries
for the patients table
"""
import phonenumbers
from sqlalchemy.types import Enum
import re
from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, DateTime, Integer, Date, TypeDecorator
from sqlalchemy.orm import relationship

class PhoneNumberType(TypeDecorator):
    impl = String(20)

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

class Patient(BaseModel, Base):
    """
    To create the patients table
    """
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    sex = Column(Enum('F', 'M'))
    DOB = Column(Date)
    email = Column(String(30), nullable=True)
    contact_no = Column(PhoneNumberType)
    address = Column(String(128), nullable=False)
    consult = relationship("Consultation", backref="patient")
    bill = relationship("Bill", backref="patient")

    def is_valid_email(email):
        """To validate email"""
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None