#!/usr/bin/python3
"""
importing necessary libraries
for consultation table
"""
from enum import Enum
from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, DateTime, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship


class FollowUpStatusEnum(Enum):
    PENDING = "Pending"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"
    NO_SHOW = "No Show"
    RESCHEDULED = "Rescheduled"
    IN_PROGRESS = "In Progress"
    FOLLOW_UP_NEEDED = "Follow-up Needed"
    CLOSED = "Closed"
    REFERRAL_SENT = "Referral Sent"
    TEST_RESULTS_PENDING = "Test Results Pending"
    MEDICATION_ADJUSTMENT = "Medication Adjustment"
    EDUCATIONAL_FOLLOW_UP = "Educational Follow-up"
    HOME_CARE = "Home Care"
    TELEHEALTH_FOLLOW_UP = "Telehealth Follow-up"
    SURGERY_SCHEDULED = "Surgery Scheduled"
    RECOVERY = "Recovery"
    POSTOPERATIVE_CARE = "Postoperative Care"
    LONG_TERM_FOLLOW_UP = "Long-term Follow-up"
    PATIENT_DISCHARGED = "Patient Discharged"

class Consultation(BaseModel, Base):
    """To create the consultation table"""
    __tablename__ = 'consultations'

    encounter_date = BaseModel.created_at.property.columns[0].copy()
    doctor_id = Column(Integer(6), ForeignKey('doctors.id'), nullable=False)
    patient_id = Column(Integer(6), ForeignKey('patients.id'), nullable=False)
    nurse_id = Column(Integer(6), ForeignKey('nurses.id'), nullable=True)
    optician_id = Column(Integer(6), ForeignKey('opticians.id'), nullable=True)
    front_desk_id = Column(Integer(6), ForeignKey('front_desks.id'), nullable=True)
    follow_up_date = Column(Date)
    follow_up_status = Column(Enum(FollowUpStatusEnum))
    test = relationship("Procedure", backref="consultation")
    bill = relationship("Bill", backref="consultation")
    drug = relationship("Drug", backref="consultation")
    accessory = relationship("Accessory", backref="consultation")
    frame = relationship("Frame", backref="consultation")