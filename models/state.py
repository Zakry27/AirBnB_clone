#!/usr/bin/python3
from models.base_model import BaseModel
"""
the Module class: State
"""


class State(BaseModel):
    """the definition for class State"""
    name = ""

    def __init__(self, *args, **kwargs):
        """ the constructor method """
        super().__init__(self, *args, **kwargs)
