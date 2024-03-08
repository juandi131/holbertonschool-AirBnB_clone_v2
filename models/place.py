#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declared_attr

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False)
                      )


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", cascade="all, delete-orphan",
                               backref='places')
        amenities = relationship("Amenity",
                                 secondary=place_amenity,
                                 back_populates='place_amenities',
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            """Returns the list of Review instances
            with place_id equals to the current Place.id"""
            from models.review import Review
            from models import storage
            listed = []
            for k, v in storage.all(Review).items():
                if v["place_id"] == self.id:
                    listed.append(v)
            return listed

        @property
        def amenities(self):
            """Returns the list of Amenity instances
            with place_id equals to the current Amenity.id"""
            from models.amenity import Amenity
            from models import storage
            listed = []
            for k, v in storage.all(Amenity).items():
                if v["place_id"] == self.id:
                    listed.append(v)
            return listed

        @amenities.setter
        def amenities(self, append):
            """ Setter attribute amenities """
            if type(append).__name__ == "Amenity":
                self.amenity_ids.append(append.id)
