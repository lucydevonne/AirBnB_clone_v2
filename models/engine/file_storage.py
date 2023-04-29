#!/usr/bin/python3
""" File Storage Module for HBNB project """
import json
from models.base_model import BaseModel


class FileStorage:
    """ Class for serializing and deserializing data to a JSON file """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """ Returns a list of objects of one type of class """
        if cls is None:
            return list(self.__objects.values())
        return [obj for obj in self.__objects.values() if isinstance(obj, cls)]

    def new(self, obj):
        """ Adds a new object to the __objects dictionary """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to JSON file """
        json_dict = {}
        for key, value in self.__objects.items():
            json_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(json_dict, f)

    def reload(self):
        """ Deserializes JSON file to __objects dictionary """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                json_dict = json.load(f)
                for key, value in json_dict.items():
                    cls_name, obj_id = key.split('.')
                    obj_dict = value
                    obj_dict['__class__'] = cls_name
                    obj = eval(cls_name)(**obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ Deletes obj from __objects """
        if obj is None:
            return
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        if key in self.__objects:
            del self.__objects[key]
