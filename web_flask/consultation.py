#!/usr/bin/python3
"""
importing necessary libraries
for consultation table
"""
from enum import Enum


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


from datetime import datetime
from routes import db


class Consultation(db.Model):
    """To create the consultation table"""
    __tablename__ = 'consultations'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    encounter_date = db.Column(db.DateTime, default=datetime.utcnow)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    nurse_id = db.Column(db.Integer, db.ForeignKey('nurses.id'), nullable=True)
    optician_id = db.Column(db.Integer, db.ForeignKey('opticians.id'), nullable=True)
    front_desk_id = db.Column(db.Integer, db.ForeignKey('front_desks.id'), nullable=True)
    follow_up_date = db.Column(db.Date, nullable=False)
    follow_up_status = db.Column(db.Enum(FollowUpStatusEnum), nullable=False)
    test = db.relationship("Procedure", backref="consultation")
    bill = db.relationship("Bill", backref="consultation")
    drug = db.relationship("Drug", backref="consultation")
    accessory = db.relationship("Accessory", backref="consultation")
    frame = db.relationship("Frame", backref="consultation")
    lens = db.relationship("Lens", backref="consultation")
    