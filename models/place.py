#!/usr/bin/python3
"""Defines the class Place."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represents a place class inherited from BaseModel.

    Attributes:
        city_id (str): Refers to the City id.
        user_id (str): Refers to the User id.
        name (str): Refers to the place's name.
        description (str): The place's description.
        number_rooms (int): Number of rooms available at place.
        number_bathrooms (int): Number of bathrooms in place.
        max_guest (int): Maximum guest capacity of the place.
        price_by_night (int): Price per night of the place.
        latitude (float): Refers to latitude of the place.
        longitude (float): Refers to longitude of the place.
        amenity_ids (list): Refers to list of Amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
