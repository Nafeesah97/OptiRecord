#!/usr/bin/python3
"""
importing necessary libraries
for procedure table
"""
from enum import Enum


class TestType(Enum):
    VISUAL_ACUITY = "VA"
    EXT_EYE_EXAM = "Preliminary external eye examination"
    SLIT_LAMP_BIOMICROSCOPY = "SLB"
    DIRECT_OPHTHALMOSCOPY = "Direct Ophthalmoscopy"
    INDIRECT_OPHTHALMOSCOPY = "Indirect Ophthalmoscopy"
    GONIOSCOPY = "Gonioscopy"
    TEAR_TEST = "Tear_test"
    OPTICAL_COHERENCE_TOMOGRAPHY = "Optical coherence tomography"
    TONOMETRY = "Tonometry"


from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.types import Enum
from models.basemodel import Base

test_types_table = Table(
    'test_types',
    Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(60), Enum(TestType))
)



from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Procedure(BaseModel, Base):
    """To create the procedure tables"""
    __tablename__ = 'procedures'
    id = Column(Integer, primary_key=True)
    consultation_id = Column(Integer, ForeignKey('consultations.id'), nullable=False)
    test_type = relationship('TestType', secondary=test_types_table, backref='procedures')
    description = Column(String(4096), nullable=False)
    diagnosis = Column(String(60), nullable=False)
    