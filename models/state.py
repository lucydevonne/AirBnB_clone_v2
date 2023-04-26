#!/usr/bin/python3
"""
Module that contains the State class which is a subclass of BaseModel
"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """
    A class for State objects.
    Inherits from BaseModel and Base.
    """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128),
                      nullable=False)
        cities = relationship("City", cascade="all, delete",
                              backref="states")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """
            Getter attribute that returns a list of City instances
            where state_id matches the current State.id.
            """
            values_city = models.storage.all("City").values()
            list_city = []
            for city in values_city:
                if city.state_id == self.id:
                    list_city.append(city)
            return list_city

