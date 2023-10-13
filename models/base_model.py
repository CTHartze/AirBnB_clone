#!/usr/bin/python3
"""Defines BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel."""

    def __init__(self, *args, **kwargs):
        """
        New BaseModel initializer.

        Args:
            *args (any): Not used.
            **kwargs (dict): Key/value attribute pairs.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """Updates and saves current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Returns the dictionary of BaseModel class instance.

        Keys are set as instance attributes, and values as attribute values.
        Additional keys in ISO-formatted string representation.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Returns the BaseModel instance in string representation method."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
