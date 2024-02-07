#!/usr/bin/python3
"""
importing necessary libraries
to create accessory table
"""
from models.basemodel import BaseModel, Base
from sqlalchemy import Column, Enum, String, Integer, ForeignKey


class OrderStatus(Enum):
    DISPENSED = "Dispensed"
    NOT_DISPENSED = "Not dispensed"
    NONCOMPLIANT = "Noncompliant"


class Accessory(BaseModel, Base):
    """To create accessory table"""
    __tablename__ = "accessories"
    stock_id = Column(Integer, ForeignKey("stocks.id"), nullable=False)
    consultation_id = Column(Integer, ForeignKey("consultations.id"), nullable=False)
    name = Column(String(60), nullable=False)
    quantity = Column(Integer)
    status = Column(String, Enum(OrderStatus))
