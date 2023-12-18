#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
import os
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
Store = os.getenv('HBNB_TYPE_STORAGE')


class Review(BaseModel, Base):
    """ Review classto store review information """
    if Store == 'db':
        __tablename__ = 'reviews'
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'))
        user_id = Column(String(60), ForeignKey('users.id'))
    else:
        place_id = ""
        user_id = ""
        text = ""
