#!/usr/bin/python3
"""Defines the class Amenity."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amenity class inherited from BaseModel.

    Attributes:
        name (str): Refers to the amenity's name.
    """

    name = ""
