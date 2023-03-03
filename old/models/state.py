#!/usr/bin/python3

"""
Defines state class that inherits
from the BaseModel
"""
from base_model import BaseModel


class State(BaseModel):
    """
    State class inherits from
    BaseModel
    """

    name: str = ""
