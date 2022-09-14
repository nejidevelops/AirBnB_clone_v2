#!/usr/bin/python3
"""
Contains the Review sub-class
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Represents Reviews"""
    place_id = ""  # will be the Place.id
    user_id = ""  # will be the User.id
    text = ""

    def __init__(self, *args, **kwargs):
        """initialize Review sub-class"""
        super().__init__(*args, **kwargs)
