#!/usr/bin/python3

""" defines a class that serializes instances to a
    JSON file and deserializes JSON files to
    instances
"""
import json
import os.path
from models.base_model import to_dict


class FileStorage:

    """
    Serializes and deserializes instances to/from JSON file. 
    """
    __file_path = "file.json"
    __objects = {}

    
    def all(self):
        """Returns the dictionary __objects. """
        return self.__objects

    def new(self, obj):

        """Sets the given obj in __objects
        with key <obj class name>.id."""

        key = type(obj).__name__ + '.' + obj.id
        self.__objects[key] = obj
        

    def save(self):
        """ Serializes __objects to the JSON file."""
        d = {}
        for key, value in self.__objects.items():
            d[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(d, file)

    def reload(self):
        """Deserializes the JSON file to __objects. """
        if not os.path.isfile(self.__file_path):
            return
        with open(self.__file_path, 'r', encoding='utf-8') as file:
            d = json.load(file)
        for key, value in d.items():
            class_name, obj_id = key.split(".")
            value = eval(class_name + "(**value)")
            self.__objects[key] = value
        
