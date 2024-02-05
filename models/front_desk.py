#!/usr/bin/python3
"""
importing necessary libraries
for the front desk table
"""
from models.patient import PhoneNumberType
import enum
import re
from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, DateTime, Integer, Date
from sqlalchemy.orm import relationship


class FrontDesk(BaseModel, Base):
    """
    To create the staffs table
    """
    __tablename__ = 'front_desks'
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    sex = Column(enum('F', 'M'))
    DOB = Column(Date)
    specialty = Column(String(60))
    Email = Column(String, nullable=False)
    contact_no = Column(PhoneNumberType)
    Address = Column(String(128), nullable=False)
    consult = relationship("Consultation", backref="front_desk")


    def is_valid_email(email):
        """To validate email"""
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None