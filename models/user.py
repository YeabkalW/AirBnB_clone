#!/usr/bin/python3

"""
defines a class that inherits from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Defines a user by various attributes
    """

    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
