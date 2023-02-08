#!/usr/bin/python3

"""Defines a class BaseModel that defines
all common attributes/methods for other
classes"""

import datetime
import uuid


class BaseModel:

    def __init__(self):
        """Initializing base class

         with public instances:
            id: holds unique id for each base model
            created_at: refers to datetime of instance creation
            updated_at: refers to datetime an instance is updated
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = datetime.datetime.now().isoformat()

    def __str__(self):
        """string method that returns
        the [<class name>] (<object uniq id>)"""

        print("[<{}>] (<{}>) <self.__dict__>"
              .format(self.__class__name, self.id))

    def save(self):
        """Updates the public instance attribute
            update_at with the current datetime

        Args:
            self

        Returns:
            updated time of the instance"""

        self.updated_at = datetime.datetime.now().isoformat()

    def to_dict(self):
        """ Returns a dictionary containing all key/values
            of __dict__ of the instance
        """
        dict = self.__dict__
        dict['__class__'] = self.__class__
        return dict
