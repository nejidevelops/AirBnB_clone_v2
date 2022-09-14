#!/usr/bin/python3
"""
Contains the City subclass
"""

from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initialize the city subclass"""
        super().__init__(*args, **kwargs)
