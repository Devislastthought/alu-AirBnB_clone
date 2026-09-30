#!/usr/bin/python3
"""Module defining BaseModel, the parent of all AirBnB clone classes."""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Defines the common attributes and methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance, or re-create one from kwargs."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """Return the string [<class name>] (<id>) <__dict__>."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at with the current datetime and save to file."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        result = dict(self.__dict__)
        result["__class__"] = self.__class__.__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result
