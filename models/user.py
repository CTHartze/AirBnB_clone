#!/usr/bin/python3
"""Defines the class User."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a User class inherited from BaseModel.

    Attributes:
        email (str): User's email.
        password (str): User's password.
        first_name (str): User's first name.
        last_name (str): User's last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
