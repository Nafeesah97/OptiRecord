#!/usr/bin/python3
"""
importing necessary libraries
for the drug table
"""
from sqlalchemy.types import Enum
from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, DateTime, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship


class Drug(BaseModel, Base):
    """To create drug table"""
    __tablename__ = "drugs"
    id = Column(Integer, primary_key=True)
    stock_id = Column(Integer, ForeignKey("stocks.id"), nullable=False)
    consultation_id = Column(Integer, ForeignKey("consultations.id"), nullable=False)
    name = Column(String(60), nullable=False)
    drug_state = Column(String, Enum('gutt', 'tab', 'oint', 'caps'))
    quantity = Column(Integer)
    Instruction = Column(String)
    status = Column(String, Enum('Dispensed', 'Not dispensed', 'Noncompliant'))
