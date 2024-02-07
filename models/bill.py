#!/usr/bin/python3
"""
importing necessary libraries
to create bill table
"""
from models.basemodel import BaseModel, Base
from sqlalchemy import Column, Float, DateTime, Integer, Date, ForeignKey


class Bill(BaseModel, Base):
    """To create the bill table"""
    __tablename__ = "bills"
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer(6), ForeignKey("patients.id"), nullable=False)
    consultation_id = Column(Integer(6), ForeignKey("consultations.id"), nullable=False)
    amount = Column(Float, nullable=False)