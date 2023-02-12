#!/usr/bin/python3

"""
Defines a class that serializes instances
to JSON file and deserializes JSON file to
instances.
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    serializes instances to JSON file
    and deserializes JSON file back to
    instance.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Public Instance Method

        Returns:
            dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets the obj in the __object dictionary
        with this format

        {'<obj class name}>.<obj id>' : obj}
        """
        key = type(obj).__name__ + '.' + obj.id
        self.__object[key] = obj

    def save(self):
        """
        converts the __objects dictionary to JSON
        file and stores it in the path referenced
        in the __file_path attribute
        """
        dict = {}
        for key, value in self.__objects.items():
            dict[key] = value.to_dict()

        with open(self.__file_path, mode="a", encoding="utf-8") as file:
            json.dump(dict, file)

    def reload(self):
        """
        converts the JSON string representation to
        dictionary __object if the file in the __file_path exists
        """

        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }

        try:

            dict = {}
            with open(self.__file_path, mode="r", encoding="utf-8") as file:
                dict = json.load(file)
            for key, value in dict.items():
                self.__objects[key] = classes[value['__class__']](**value)

        except FileNotFoundError:
            pass
