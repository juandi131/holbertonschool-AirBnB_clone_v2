#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import os
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
STORE = os.getenv('HBNB_TYPE_STORAGE')


class Amenity(BaseModel, Base):
    if STORE == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenity = relationship('Place', secondary='place_amenity')
    else:
        name = ""
