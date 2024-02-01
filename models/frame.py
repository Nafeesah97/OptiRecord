#!/usr/bin/python3
"""
importing necessary libraries
to create frame table
"""
from enum import Enum
from models.basemodel import BaseModel, Base
from sqlalchemy import Column, Float, String, Integer, Date, ForeignKey


class Frame(BaseModel, Base):
    """To create frame table"""
    __tablename__ = "frames"
    stock_id = Column(Integer(6), ForeignKey("stocks.id"), nullable=False)
    consultation_id = Column(Integer(6), ForeignKey("consultations.id"), nullable=False)
    name = Column(String(60), nullable=False)
    shape = Column(String(60), nullable=True)
    colour = Column(String(60), nullable=True)
    material = Column(String(60), nullable=True)
    quantity = Column(Integer)
    status = Column(String, Enum('Dispensed', 'Not dispensed', 'Noncompliant'))
