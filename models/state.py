#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
import shlex
from sqlalchemy.ext.declarative import declarative_base


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        vari = models.storage.all()
        liste = []
        res = []
        for k in vari:
            city = k.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                listE.append(vari[k])
        for el in liste:
            if (el.state_id == self.id):
                res.append(el)
        return (res)
