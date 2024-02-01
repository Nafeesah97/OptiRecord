#!/usr/bin/python3
"""
initializes models package
"""
from models.engine.database import DBStorage
storage = DBStorage()

storage.reload()
