#!/usr/bin/python3

"""
Defines Amenity class that inherits
from the BaseModel
"""
from base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class that inherits from
    BaseModel
    """
    name: str = ""
