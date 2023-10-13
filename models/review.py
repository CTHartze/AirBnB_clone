#!/usr/bin/python3
"""Defines the class Review."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review class inherited from BaseModel.

    Attributes:
        place_id (str): Refers to the Place id.
        user_id (str): Refers to the User id.
        text (str): Refers to the review's text.
    """

    place_id = ""
    user_id = ""
    text = ""
