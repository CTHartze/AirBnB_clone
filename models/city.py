#!/usr/bin/python3
"""Defines the class City."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city class inherited from BaseModel.

    Attributes:
        state_id (str): The <State.id>.
        name (str): Refers to the city's name.
    """

    state_id = ""
    name = ""
