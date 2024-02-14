#!/usr/bin/python3
"""
importing necessary libraries
for the user table
"""
from models.patient import PhoneNumberType
from sqlalchemy.types import Enum
import re
from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, DateTime, Integer, Date
from sqlalchemy.orm import relationship
from flask_login import UserMixin


class User(BaseModel, Base, UserMixin):
    """
    To create the staffs table
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True, nullable=False)
    Email = Column(String, unique=True, nullable=False)
    image_file = Column(String(20), nullable=False, default='default.png')
    password = Column(String(60), nullable=False)

    def is_valid_email(email):
        """To validate email"""
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"