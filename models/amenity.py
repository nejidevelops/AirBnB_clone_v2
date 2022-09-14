#!/usr/bin/python3
"""
The Amenity child-class
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amenity"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initialize Amenity subclass"""
        super().__init__(*args, **kwargs)
