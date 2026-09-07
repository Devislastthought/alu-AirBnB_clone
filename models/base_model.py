#!/usr/bin/python3
"""The common parent class for all AirBnB objects."""

from datetime import datetime
import uuid

from models import storage


class BaseModel:
    """Store an object's ID, dates, and shared save/convert behaviour."""

    def __init__(self, *args, **kwargs):
        """Create a new object or rebuild one from a dictionary."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            now = datetime.now()
            self.id = str(uuid.uuid4())
            self.created_at = now
            self.updated_at = now
            storage.new(self)

    def __str__(self):
        """Return a readable description of this object."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """Update the date and save this object to the JSON file."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return this object's data in a JSON-friendly dictionary."""
        result = self.__dict__.copy()
        result["__class__"] = self.__class__.__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result
