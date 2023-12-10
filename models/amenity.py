#!/usr/bin/python3
from models.base_model import BaseModel
"""
the Module class: Amenity
"""


class Amenity(BaseModel):
    """the definition for class Amenity"""
    name = ""

    def __init__(self, *args, **kwargs):
        """ the constructor method """
        super().__init__(self, *args, **kwargs)
