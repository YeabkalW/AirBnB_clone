#!/usr/bin/python3

"""Defines a class BaseModel that defines
all common attributes/methods for other
classes"""

import datetime
import uuid
import __init__


class BaseModel:

    def __init__(self, *args, **kwargs):
        """Initializing base class

         with public instances:
            id: holds unique id for each base model
            created_at: refers to datetime of instance creation
            updated_at: refers to datetime an instance is updated
        """
        if kwargs:

            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                setattr(self, key, value)

                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.datetime.strptime
                            (value, '%Y-%m-%dT%H:%M:%S.%f'))

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

        __init__.storage.new(self)

    def __str__(self):
        """string method that returns
        the [<class name>] (<object uniq id>)"""

        print("[{}] ({}) {}"
              .format(self.__class__name, self.id, self.__dict__))

    def save(self):
        """Updates the public instance attribute
            update_at with the current datetime

        Args:
            self

        Returns:
            updated time of the instance"""

        self.updated_at = datetime.datetime.now().isoformat()
        __init__.storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all key/values
            of __dict__ of the instance
        """
        ob_dict = self.__dict__.copy()
        ob_dict['__class__'] = self.__class__.__name__
        ob_dict['created_at'] = self.created_at.isoformat()
        ob_dict['updated_at'] = self.updated_at.isoformat()
        return ob_dict
