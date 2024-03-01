#!/usr/bin/python3
"""
importing necessary libraries
to create accessory table
"""
from routes import db


class Accessory(db.Model):
    """To create accessory table"""
    __tablename__ = "accessories"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stock_id = db.Column(db.Integer, db.ForeignKey("stocks.id"), nullable=False)
    consultation_id = db.Column(db.Integer, db.ForeignKey("consultations.id"), nullable=False)
    name = db.Column(db.String(60), nullable=False)
    quantity = db.Column(db.Integer)
    status = db.Column(db.String(20), db.Enum("Dispensed", "Not dispensed", "Noncompliant"))
