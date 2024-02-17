#!/usr/bin/python3
"""
importing necessary libraries
to create accessory table
"""

from sqlalchemy.types import Enum
from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey


class Accessory(BaseModel, Base):
    """To create accessory table"""
    __tablename__ = "accessories"
    id = Column(Integer, primary_key=True)
    stock_id = Column(Integer, ForeignKey("stocks.id"), nullable=False)
    consultation_id = Column(Integer, ForeignKey("consultations.id"), nullable=False)
    name = Column(String(60), nullable=False)
    quantity = Column(Integer)
    status = Column(String(20), Enum("Dispensed", "Not dispensed", "Noncompliant"))
