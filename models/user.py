#!/usr/bin/python3
"""
the module for User class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    the class User that handles users' information
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
