#!/usr/bin/python3
"""
importing necessary libraries
for the procedure table
"""

from routes import db, Base
from enum import Enum as En

class TestType(En):
    VISUAL_ACUITY = "VA"
    EXT_EYE_EXAM = "Preliminary external eye examination"
    SLIT_LAMP_BIOMICROSCOPY = "SLB"
    DIRECT_OPHTHALMOSCOPY = "Direct Ophthalmoscopy"
    INDIRECT_OPHTHALMOSCOPY = "Indirect Ophthalmoscopy"
    GONIOSCOPY = "Gonioscopy"
    TEAR_TEST = "Tear_test"
    OPTICAL_COHERENCE_TOMOGRAPHY = "Optical coherence tomography"
    TONOMETRY = "Tonometry"

test_types_table = db.Table(
    'test_types',
    Base.metadata,
    db.Column('id', db.Integer, primary_key=True),
    db.Column('name', db.Enum(TestType))
)

class Procedure(db.Model):
    """To create the procedure tables"""
    __tablename__ = 'procedures'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    consultation_id = db.Column(db.Integer, db.ForeignKey('consultations.id'), nullable=False)
    test_type = db.Column(db.Enum(TestType), nullable=False)
    description = db.Column(db.String(4096), nullable=False)
    diagnosis = db.Column(db.String(60), nullable=False)
