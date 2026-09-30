#!/usr/bin/python3
"""Unit tests for the BaseModel class."""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel."""

    def test_id_is_unique_string(self):
        """Each instance gets a different string id."""
        a, b = BaseModel(), BaseModel()
        self.assertIsInstance(a.id, str)
        self.assertNotEqual(a.id, b.id)

    def test_datetimes(self):
        """created_at and updated_at are datetime objects."""
        obj = BaseModel()
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_str(self):
        """__str__ has the expected format."""
        obj = BaseModel()
        expected = "[BaseModel] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(str(obj), expected)

    def test_save_updates_time(self):
        """save() changes updated_at."""
        obj = BaseModel()
        before = obj.updated_at
        obj.save()
        self.assertGreater(obj.updated_at, before)

    def test_to_dict(self):
        """to_dict() returns the right keys and ISO strings."""
        obj = BaseModel()
        obj.name = "test"
        d = obj.to_dict()
        self.assertEqual(d["__class__"], "BaseModel")
        self.assertEqual(d["name"], "test")
        self.assertEqual(d["created_at"], obj.created_at.isoformat())
        self.assertEqual(d["updated_at"], obj.updated_at.isoformat())
        self.assertIsInstance(d["id"], str)

    def test_from_dict(self):
        """An instance can be re-created from its dictionary."""
        obj = BaseModel()
        obj.number = 89
        new = BaseModel(**obj.to_dict())
        self.assertIsNot(obj, new)
        self.assertEqual(obj.id, new.id)
        self.assertEqual(new.number, 89)
        self.assertEqual(obj.created_at, new.created_at)
        self.assertIsInstance(new.updated_at, datetime)
        self.assertFalse(hasattr(new, "__class__") and
                         "__class__" in new.__dict__)

    def test_args_ignored(self):
        """Positional arguments are not used."""
        obj = BaseModel(1, 2, 3)
        self.assertIsInstance(obj.id, str)


if __name__ == "__main__":
    unittest.main()
