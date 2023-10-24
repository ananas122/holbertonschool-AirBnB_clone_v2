#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from models import storage
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="all, delete",
                            passive_deletes=True)
    else:
        @property
        def cities(self):
            """returns the list of City instances"""
            all_cities = storage.all(City)
            return [
                element
                for element in all_cities.values()
                if self.id == element.state_id
            ]