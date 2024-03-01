#!/usr/bin/python3
"""
importing necessary libraries
for stock table
"""
from routes import db

class Stock(db.Model):
    """To create the stock table"""
    __tablename__ = "stocks"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60), nullable=False)
    category = db.Column(db.String(15), db.Enum('Lens', 'Frame', 'Accessory', 'Drug'), nullable=False)
    availability = db.Column(db.String(15), db.Enum('In stock', 'Out of stock'), nullable=False)
    drug = db.relationship("Drug", backref="stock")
    accessory = db.relationship("Accessory", backref="stock")
    frame = db.relationship("Frame", backref="stock")
    lens = db.relationship("Lens", backref="stock")
