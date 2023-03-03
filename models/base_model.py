#!/usr/bin/python3
""" this is the base module for airbnb project """

import uuid
from datetime import datetime
from models import storage

class BaseModel():
    """
    this BaseModel class will """

    def __init__(self, *args, **kwargs):
        self.created_at = datetime.today()
        self.id = str(uuid.uuid4())
        self.updated_at = self.created_at
        for key in kwargs:
            if key != "__class__":
                if (key in ["created_at", "updated_at"]):
                    ss = "%Y-%m-%dT%H:%M:%S.%f"
                    setattr(self, key, datetime.strptime(kwargs[key], ss))

                else:
                    setattr(self, key, kwargs[key])

        storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format("BaseModel", self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        res = (self.__dict__).copy()
        res["__class__"] = "BaseModel"
        temp = self.created_at
        res["created_at"] = temp.isoformat()
        temp = self.updated_at
        res["updated_at"] = temp.isoformat()
        return res
