#!/usr/bin/python3
"""the user class
"""

from models.base_model import BaseModel
import json


class User(BaseModel):
    '''the base model class'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
