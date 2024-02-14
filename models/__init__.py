#!/usr/bin/python3
"""
Initializes models package
"""
from models.engine.database import DBStorage

storage = DBStorage()
storage.reload()
