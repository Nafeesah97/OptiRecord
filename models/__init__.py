#!/usr/bin/python3
"""
Initializes models package
"""
from models.engine.database import DBStorage

def initialize_storage():
    """
    Initializes the storage object
    """
    storage = DBStorage()
    storage.reload()
    return storage

# Initialize storage lazily
storage = None

if __name__ == "__main__":
    # Example usage
    storage = initialize_storage()
