#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place
from sqlalchemy.ext.declarative import declarative_base


class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="cities")
