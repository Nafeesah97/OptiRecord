#!/usr/bin/python3
"""
importing necessary libraries
for the drug table
"""
from routes import db


class Drug(db.Model):
    """To create drug table"""
    __tablename__ = "drugs"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stock_id = db.Column(db.Integer, db.ForeignKey("stocks.id"), nullable=False)
    consultation_id = db.Column(db.Integer, db.ForeignKey("consultations.id"), nullable=False)
    name = db.Column(db.String(60), nullable=False)
    drug_state = db.Column(db.String(15), db.Enum('gutt', 'tab', 'oint', 'caps'))
    quantity = db.Column(db.Integer)
    Instruction = db.Column(db.String(4098))
    status = db.Column(db.String(20), db.Enum('Dispensed', 'Not dispensed', 'Noncompliant'))
