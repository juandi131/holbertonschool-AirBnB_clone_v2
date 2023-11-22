#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import os
STORE = os.getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ State class """
    if STORE == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)

        cities = relationship('City',
                              backref='state',
                              cascade='all, delete, delete-orphan')

    else:
        name = ""

        @property
        def cities(self):
            """ gets cities """
            from models.city import City
            from models import storage
            di = storage.all(City).values()
            new_di = []
            for obj in di:
                if obj.state_id == self.id:
                    new_di.append(obj)
            return new_di
