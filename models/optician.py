#!/usr/bin/python3
"""
importing necessary libraries
for the optician table
"""
from models.patient import PhoneNumberType
from sqlalchemy.types import Enum
import re
from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, DateTime, Integer, Date
from sqlalchemy.orm import relationship


class Optician(BaseModel, Base):
    """
    To create the staffs table
    """
    __tablename__ = 'opticians'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    sex = Column(Enum('F', 'M'))
    DOB = Column(Date)
    Email = Column(String, nullable=False)
    contact_no = Column(PhoneNumberType)
    Address = Column(String(128), nullable=False)
    consult = relationship("Consultation", backref="optician")


    def is_valid_email(email):
        """To validate email"""
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None