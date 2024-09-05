#!/usr/bin/python3
"""
State class for managing states.
"""

from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City

class State(BaseModel, Base):
    """
    State class to manage states in the database.
    """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete-orphan')

    def cities(self):
        """
        Returns a list of City objects linked to the current State.
        """
        if type(storage) is not DBStorage:
            return [city for city in storage.all(City).values() if city.state_id == self.id]
        return self.cities

