#!/usr/bin/python3
from models.base_model import BaseModel
from models.place import Place
from models.user import User
"""
the Module class: Review
"""


class Review(BaseModel):
    """the definition for class Review"""
    text = ""
    place_id = ""
    user_id = ""

    def __init__(self, *args, **kwargs):
        """ the constructor method """
        super().__init__(self, *args, **kwargs)
