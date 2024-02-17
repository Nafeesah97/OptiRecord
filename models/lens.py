#!/usr/bin/python3
"""
importing necessary libraries
to create lens table
"""
from sqlalchemy.types import Enum
from models.basemodel import BaseModel, Base
from sqlalchemy import CheckConstraint, Column, Float, String, Integer, Date, ForeignKey


class Lens(BaseModel, Base):
    """To create lens table"""
    __tablename__ = "lenses"
    id = Column(Integer, primary_key=True)
    stock_id = Column(Integer, ForeignKey("stocks.id"), nullable=False)
    consultation_id = Column(Integer, ForeignKey("consultations.id"), nullable=False)
    sphere_power_right = Column(Float)
    sphere_power_left = Column(Float)
    cylinder_power_right = Column(Float)
    cylinder_power_left = Column(Float)
    axis_right = Column(Integer, CheckConstraint('axis_right >= 0 AND axis_right <= 180'))
    axis_left = Column(Integer, CheckConstraint('axis_left >= 0 AND axis_left <= 180'))
    ADD_right = Column(Float)
    ADD_left = Column(Float)
    base_curve_right = Column(Float, nullable=True)
    base_curve_left = Column(Float, nullable=True)
    diameter_right = Column(Float, nullable=True)
    diameter_left = Column(Float, nullable=True)
    lens_type = Column(String(20))
    quantity = Column(Integer)
    status = Column(String(20), Enum('Dispensed', 'Not dispensed', 'Noncompliant'))
