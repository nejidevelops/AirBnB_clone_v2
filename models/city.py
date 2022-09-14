#!/usr/bin/python3
""" Defines  city class."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """
    Represents class.
    Attributes:
        __tablename__ (str): The name of the MySQL table.
        state_id (str): The id of the state.
        name (str): The name of the state.
        places (sqlalchemy relationship): The User-Place relationship.
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")
