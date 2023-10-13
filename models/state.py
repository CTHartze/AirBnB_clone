#!/usr/bin/python3
"""Defines the class State."""
from models.base_model import BaseModel


class State(BaseModel):
    """Represents a state class inherited from BaseModel.

    Attributes:
        name (str):Refers to the state's name.
    """

    name = ""
