#!/usr/bin/python3
"""
importing necessary libraries
to create bill table
"""
from routes import db


class Bill(db.Model):
    """To create the bill table"""
    __tablename__ = "bills"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    patient_id = db.Column(db.Integer, db.ForeignKey("patients.id"), nullable=False)
    consultation_id = db.Column(db.Integer, db.ForeignKey("consultations.id"), nullable=False)
    amount = db.Column(db.Float, nullable=False)