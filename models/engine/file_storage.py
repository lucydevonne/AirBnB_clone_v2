import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        if cls:
            return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
        else:
            return self.__objects

    def new(self, obj):
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(new_dict, file)

    def reload(self):
        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State

        class_dict = {"BaseModel": BaseModel, "User": User, "Amenity": Amenity,
                      "City": City, "Place": Place, "Review": Review, "State": State}

        try:
            with open(self.__file_path, "r") as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    obj_class = class_dict[value['__class__']]
                    self.__objects[key] = obj_class(**value)
        except:
            pass

    def delete(self, obj=None):
        if obj is None:
            return
        key = obj.__class__.__name__ + "." + obj.id
        if key in self.__objects:
            del self.__objects[key]

    def close(self):
        self.reload()
