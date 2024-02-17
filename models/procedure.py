from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.types import Enum
from models.basemodel import Base
from sqlalchemy.orm import relationship
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

test_types_table = Table(
    'test_types',
    Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(60), Enum(TestType))
)

class Procedure(Base):
    """To create the procedure tables"""
    __tablename__ = 'procedures'
    id = Column(Integer, primary_key=True)
    consultation_id = Column(Integer, ForeignKey('consultations.id'), nullable=False)
    test_type = Column(Enum(TestType), nullable=False)  
    description = Column(String(4096), nullable=False)
    diagnosis = Column(String(60), nullable=False)
