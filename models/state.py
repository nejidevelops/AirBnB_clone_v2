#!/usr/bin/python3
"""
The state child-class
"""


from models.base_model import BaseModel


class State(BaseModel):
    """Represents a state"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initialize state subclass"""
        super().__init__(*args, **kwargs)
