#!/usr/bin/python3
from models.base_model import BaseModel
"""
the Module class: City
"""


class City(BaseModel):
    """the definition for class City"""
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """ the constructor method """
        super().__init__(self, *args, **kwargs)
