#!/usr/bin/python3
"""
this defines place module
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """place class
    attributes:
    cities id
    users id
    places name
    description of the place
    num of rooms
    num of bathrooms
    max num of guests
    price by night
    latitude of the place
    longitude of place
    list of ids of the amenity
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
