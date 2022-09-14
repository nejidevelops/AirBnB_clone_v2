#!/usr/bin/python3
""" Defines all common attributes/methods."""
import models
from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """ Represents the BaseModel of the AirBnB project.

    Attributes:
        id (sqlalchemy String): The BaseModel id.
        created_at (sqlalchemy DateTime): The datetime at creation.
        updated_at (sqlalchemy DateTime): The datetime of last update.
    """

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel.

        Args:
            *args (any): Won't be used.
            **kwargs (dict): Key/Value pairsof the attributes.
        """
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.utcnow()

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """ Return the print/str representation the BaseModel instance. """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime.
        """
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of
        __dict__ of the instance.
        """
        rdict = self.__dict__.copy()
        rdict["__class__"] = str(type(self).__name__)
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict.pop("_sa_instance_state", None)

        return rdict

    def delete(self):
        """ Delete the current instance from the storage (models.storage)
        by calling the method delete
        """
        models.storage.delete(self)
