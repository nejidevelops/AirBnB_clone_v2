#!/usr/bin/python3
"""
the user childclass
"""


from models.base_model import BaseModel


class User(BaseModel):
    """Representation of a user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes the user"""
        super().__init__(*args, **kwargs)
