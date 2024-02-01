#!/usr/bin/python3
"""
contains the database storage methods
"""


from sqlalchemy import create_engine 
from sqlalchemy.orm import scoped_session, sessionmaker
from models.basemodel import Base
import os
from os import getenv


classes = {}

class DBStorage():
    """The class to interact with the server"""

    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        OPTI_MYSQL_USER = getenv('OPTI_MYSQL_USER')
        OPTI_MYSQL_PWD = getenv('OPTI_MYSQL_PWD')
        OPTI_MYSQL_HOST = getenv('OPTI_MYSQL_HOST')
        OPTI_MYSQL_DB = getenv('OPTI_MYSQL_DB')
        OPTI_ENV = getenv('OPTI_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(OPTI_MYSQL_USER,
                                             OPTI_MYSQL_PWD,
                                             OPTI_MYSQL_HOST,
                                             OPTI_MYSQL_DB))
        if OPTI_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """To display all database content or a particular class"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                val = self.__session.query(classes[clss]).all()
                for obj in val:
                    val_id = obj.__class__.__name__ + '.' + obj.id
                new_dict[val_id] = val
        return new_dict

    def new(self, obj):
        """To add a new object"""
        self.__session.add(obj)

    def save(self):
        """To save changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """To delete a particular data from the database"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """To reload the database i.e create tables"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """To close a current session"""
        self.__session.close()

    def get(self, cls, id):
        """To get a particular class and id"""
        if cls in classes.values():
            obj = self.__session.query(cls).filter_by(id=id)
            return obj
        else:
            return None
        
    def count(self, cls=None):
        """Count the number of class data or all data"""
        count = 0
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                count += self.__session.query(classes[clss]).count()
        
        return count