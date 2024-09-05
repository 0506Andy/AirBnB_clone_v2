#!/usr/bin/python3
"""
Storage engine for handling file-based storage.
"""

import json
from models.base_model import BaseModel
from models.city import City
from models.state import State

class FileStorage:
    """
    FileStorage class to manage storage of objects.
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Returns the dictionary of objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the storage.
        """
        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file.
        """
        with open(self.__file_path, 'w') as file:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, file)

    def reload(self):
        """
        Deserializes the JSON file to objects.
        """
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for k, v in obj_dict.items():
                    cls_name = v['__class__']
                    cls = globals()[cls_name]
                    self.__objects[k] = cls(**v)
        except FileNotFoundError:
            pass

    def close(self):
        """
        Calls reload() method to deserialize objects.
        """
        self.reload()

