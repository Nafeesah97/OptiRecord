#!/usr/bin/python3
"""
importing necessary libraries
for stock table
"""
from sqlalchemy.types import Enum
from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, DateTime, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship


class Stock(BaseModel, Base):
    """To create the stock table"""
    __tablename__ = "stocks"
    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    category = Column(String(15), Enum('Lens', 'Frame', 'Accessory', 'Drug'), nullable=False)
    availability = Column(String(15), Enum('In stock', 'Out of stock'), nullable=False)
    drug = relationship("Drug", backref="stock")
    accessory = relationship("Accessory", backref="stock")
    frame = relationship("Frame", backref="stock")
    lens = relationship("Lens", backref="stock")
