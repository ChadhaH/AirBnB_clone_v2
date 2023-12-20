#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import environ as env
import models
from sqlalchemy.ext.declarative import declarative_base


place_amenity = Table(
    'place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey("places.id"), primary_key=True,
            nullable=False),
    Column('amenity_id', String(60), ForeignKey("amenities.id"),
            primary_key=True, nullable=False)
    )


class Place(BaseModel, Base):
    """ The Class for Place """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    reviews = relationship("Review", cascade='all, delete, delete-orphan',
                            backref="place")
    amenities = relationship("Amenity", secondary=place_amenity,
                              viewonly=False, back_populates="place_amenities")

    @property
    def reviews(self):
        """get all refiews with the current place id
        from filestorage
        """
        if env.get('HBNB_TYPE_STORAGE') == 'db':
            return self.__reviews
        liste = [
            value for key, value in models.storage.all(models.Review).items()
            if value.place_id == self.id
        ]
        return (liste)

    @property
    def amenities(self):
        """get all amenities with the current place id
        """
        if env.get('HBNB_TYPE_STORAGE') == 'db':
            return self.__amenities
        liste = [
            value for key, value in models.storage.all(models.Amenity).items()
            if value.id in self.amenity_ids
        ]
        return (liste)
