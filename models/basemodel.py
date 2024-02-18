#!/usr/bin/python3
"""
importing necessary libraries
to create base model
"""
from models import storage
from datetime import datetime
from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel(Base):
    """The base class for the tables"""
    __abstract__ = True  # Set abstract attribute to True

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def validate_id_value(self, value):
        """To ensure id value is a positive integer"""
        return max(1, min(value, 999999))

    @property
    def id(self):
        """to get the id"""
        return self._id

    @id.setter
    def id(self, value):
        """To set id to the 6 digits"""
        self._id = self.validate_id_value(value)

    def __str__(self):
        """Format id with the leading zeros"""
        return f"{self.id:06d}"

    def save(self):
        """updates the attribute 'updated_at' with the current datetime and saves the instance"""
        self.updated_at = datetime.utcnow()
        storage.add(self)
        storage.save()

    def delete(self):
        """deletes a current instance"""
        storage.delete(self)
        storage.save()
