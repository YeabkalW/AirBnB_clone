#!/usr/bin/python3

"""
Defines City class that inherits from
BaseModel
"""

from base_model import BaseModel


class City(BaseModel):
    """
    city class that inherits from BaseModel
    """

    state_id: str = ""
    name: str = ""
