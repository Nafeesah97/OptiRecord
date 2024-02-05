#!/usr/bin/python3
"""
Contains the base for other class
"""


from datetime import datetime
from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """The base class for the tables"""
    def default_value():
        """To start id from 1"""
        return 1
    
    id = Column(Integer(6), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    @staticmethod
    def validate_id_value(value):
        """To ensure id value is a 6-digit"""
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
        from models import storage
        """updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def delete(self):
        from models import storage
        """deletes a current instance"""
        storage.delete(self)