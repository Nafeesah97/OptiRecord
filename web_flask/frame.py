#!/usr/bin/python3
"""
importing necessary libraries
to create frame table
"""
from routes import db


class Frame(db.Model):
    """To create frame table"""
    __tablename__ = "frames"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stock_id = db.Column(db.Integer, db.ForeignKey("stocks.id"), nullable=False)
    consultation_id = db.Column(db.Integer, db.ForeignKey("consultations.id"), nullable=False)
    name = db.Column(db.String(60), nullable=False)
    shape = db.Column(db.String(60), nullable=True)
    colour = db.Column(db.String(60), nullable=True)
    material = db.Column(db.String(60), nullable=True)
    quantity = db.Column(db.Integer)
    status = db.Column(db.String(20), db.Enum('Dispensed', 'Not dispensed', 'Noncompliant'))
