#!/usr/bin/python3
"""
tis is the Module for City class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents city.

    Attributes:
        state_id (str): this is the state id.
        name (str): name of the city.
    """

    state_id = ""
    name = ""
