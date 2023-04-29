#!/usr/bin/python3
"""
FileStorage Module for HBNB project
"""

import json
import os.path


class FileStorage:
    """
    FileStorage class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Returns a dictionary with all objects
        """
        if cls is None:
            return self.__objects
        else:
            obj_dict = {}
            for key, value in self.__objects.items():
                if isinstance(value, cls):
                    obj_dict[key] = value
            return obj_dict

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = key.split('.')[0]
                    obj = eval(class_name + '(**value)')
                    self.__objects[key] = obj

    def delete(self, obj=None):
        """
        Deletes obj from __objects
        """
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            del self.__objects[key]
            self.save()
