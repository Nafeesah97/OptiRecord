#!/usr/bin/python3
"""
importing necessary libraries
to create accessory table
"""
from enum import Enum
from models.basemodel import BaseModel, Base
from sqlalchemy import Column, Float, String, Integer, Date, ForeignKey


class Accessory(BaseModel, Base):
    """To create accessory table"""
    __tablename__ = "accessories"
    stock_id = Column(Integer(6), ForeignKey("stocks.id"), nullable=False)
    consultation_id = Column(Integer(6), ForeignKey("consultations.id"), nullable=False)
    name = Column(String(60), nullable=False)
    quantity = Column(Integer)
    status = Column(String, Enum('Dispensed', 'Not dispensed', 'Noncompliant'))
