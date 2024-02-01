#!/usr/bin/python3
"""
importing necessary libraries
for procedure table
"""
from ast import Set
from enum import Enum
from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class TestType(Set):
    VISUAL_ACUITY = "VA"
    EXT_EYE_EXAM = "Preliminary external eye examination"
    SLIT_LAMP_BIOMICROSCOPY = "SLB"
    DIRECT_OPHTHALMOSCOPY = "Direct Ophthalmoscopy"
    INDIRECT_OPHTHALMOSCOPY = "Indirect Ophthalmoscopy"
    GONIOSCOPY = "Gonioscopy"
    TEAR_TEST = "Tear_test"
    OPTICAL_COHERENCE_TOMOGRAPHY = "Optical coherence tomography"
    TONOMETRY = "Tonometry"



class Procedure(BaseModel, Base):
    """To create the procedure tables"""
    __tablename__ = 'procedures'
    consultation_id = Column(Integer(6), ForeignKey('consultations.id'), nullable=False)
    test_type = Column(String(60), Set(TestType), nullable=False)
    description = Column(String(4096), nullable=False)
    diagnosis = Column(String(60), nullable=False)
    