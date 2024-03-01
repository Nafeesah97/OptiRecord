#!/usr/bin/python3
"""
importing necessary libraries
to create lens table
"""
from routes import db


class Lens(db.Model):
    """To create lens table"""
    __tablename__ = "lenses"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stock_id = db.Column(db.Integer, db.ForeignKey("stocks.id"), nullable=False)
    consultation_id = db.Column(db.Integer, db.ForeignKey("consultations.id"), nullable=False)
    sphere_power_right = db.Column(db.Float)
    sphere_power_left = db.Column(db.Float)
    cylinder_power_right = db.Column(db.Float)
    cylinder_power_left = db.Column(db.Float)
    axis_right = db.Column(db.Integer, db.CheckConstraint('axis_right >= 0 AND axis_right <= 180'))
    axis_left = db.Column(db.Integer, db.CheckConstraint('axis_left >= 0 AND axis_left <= 180'))
    ADD_right = db.Column(db.Float)
    ADD_left = db.Column(db.Float)
    base_curve_right = db.Column(db.Float, nullable=True)
    base_curve_left = db.Column(db.Float, nullable=True)
    diameter_right = db.Column(db.Float, nullable=True)
    diameter_left = db.Column(db.Float, nullable=True)
    lens_type = db.Column(db.String(20))
    quantity = db.Column(db.Integer)
    status = db.Column(db.String(20), db.Enum('Dispensed', 'Not dispensed', 'Noncompliant'))
