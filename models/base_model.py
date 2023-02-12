#!/usr/bin/python3

"""
Defines a class BaseModel that defines
all common attributes/methods for other
classes
"""

import uuid
import datetime
from __init__ import storage


class BaseModel:
    def __init__(self, *args, **kwargs):

        """
        Initializing base class

        with public instances:
            id: holds unique id for each base model
            created_at: refers to datetime of instance creation
            updated_at: refers to datetime an instance is updated
        """

        if kwargs:

            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.datetime.strptime
                            (value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):

        """
        Method is called automatically when print
        or str method is used

        Returns:
            [<class name>] (<self.id) <self.__dict__>
        """

        return "[{}] ({}) {}"\
               .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute
        with current time
        """

        self.updated_at = datetime.datetime.now()
        storage.save(self)

    def to_dict(self):
        """
        converts instance attributes to
        dictionary of that object.

        Returns:
            a dictionary containing all
            keys/values of the instance.
        """
        obj_dict = dict(self.__dict__)
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
