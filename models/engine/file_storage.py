#!/usr/bin/python3
"""Save and reload AirBnB objects in a JSON file."""

import json
from datetime import datetime


class FileStorage:
    """Store model dictionaries in file.json and rebuild model objects."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return all objects currently in memory."""
        return self.__objects

    def new(self, obj):
        """Add an object to memory using ClassName.id as its key."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Write every object to the JSON file."""
        data = {key: value.to_dict()
                for key, value in self.__objects.items()}
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(data, file)

    def reload(self):
        """Load objects from file.json when the file exists."""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            return

        classes = {
            "BaseModel": "models.base_model.BaseModel",
            "User": "models.user.User",
            "State": "models.state.State",
            "City": "models.city.City",
            "Amenity": "models.amenity.Amenity",
            "Place": "models.place.Place",
            "Review": "models.review.Review",
        }
        for value in data.values():
            class_name = value["__class__"]
            module_name, object_name = classes[class_name].rsplit(".", 1)
            module = __import__(module_name, fromlist=[object_name])
            self.new(getattr(module, object_name)(**value))
