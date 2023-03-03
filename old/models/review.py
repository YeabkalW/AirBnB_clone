#!/usr/bin/python3

"""
defines Review class that inherits from
BaseModel
"""

from base_model import BaseModel


class Review(BaseModel):
    """
    defines Review class that inherits from
    BaseModel
    """

    place_id: str = ""
    user_id: str = ""
    text: str = ""
