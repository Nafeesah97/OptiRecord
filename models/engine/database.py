#!/usr/bin/python3
"""
contains the database storage methods
"""
import os
from os import getenv
from web_flask.accessory import Accessory
from web_flask.bill import Bill
from web_flask.consultation import Consultation
from web_flask.doctor import Doctor
from web_flask.drug import Drug
from web_flask.frame import Frame 
from web_flask.front_desk import FrontDesk
from web_flask.lens import Lens
from web_flask.nurse import Nurse
from web_flask.optician import Optician
from web_flask.patient import Patient
from web_flask.procedure import Procedure
from web_flask.stock import Stock
from web_flask.routes import Base, db

classes = {"Accessory": Accessory, "Bill": Bill, "Consultation": Consultation,
           "Doctor": Doctor, "Drug": Drug, "Frame": Frame, "FrontDesk": FrontDesk,
           "Lens": Lens, "Nurse": Nurse, "Optician": Optician, "Patient": Patient,
           "Procedure": Procedure, "Stock": Stock}

class DBStorage():
    """The class to interact with the server"""

    __engine = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        OPTI_MYSQL_USER = getenv('OPTI_MYSQL_USER')
        OPTI_MYSQL_PWD = getenv('OPTI_MYSQL_PWD')
        OPTI_MYSQL_HOST = getenv('OPTI_MYSQL_HOST')
        OPTI_MYSQL_DB = getenv('OPTI_MYSQL_DB')
        OPTI_ENV = getenv('OPTI_ENV')
        self.__engine = db.create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                         format(OPTI_MYSQL_USER,
                                                OPTI_MYSQL_PWD,
                                                OPTI_MYSQL_HOST,
                                                OPTI_MYSQL_DB))

        # Bind the session to the app
        db.session.bind = self.__engine

    def all(self, cls=None):
        """To display all database content or a particular class"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                val = db.session.query(classes[clss]).all()
                for obj in val:
                    val_id = obj.__class__.__name__ + '.' + obj.id
                    new_dict[val_id] = val
        return new_dict

    def new(self, obj):
        """To add a new object"""
        db.session.add(obj)

    def save(self):
        """To save changes"""
        db.session.commit()

    def delete(self, obj=None):
        """To delete a particular data from the database"""
        if obj is not None:
            db.session.delete(obj)

    def reload(self):
        """To reload the database i.e create tables"""
        Base.metadata.create_all(self.__engine)

    def close(self):
        """To close a current session"""
        db.session.close()

    def get(self, cls, id):
        """To get a particular class and id"""
        if cls in classes.values():
            obj = db.session.query(cls).filter_by(id=id).first()
            return obj
        else:
            return None

    def count(self, cls=None):
        """Count the number of class data or all data"""
        count = 0
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                count += db.session.query(classes[clss]).count()
        return count
    