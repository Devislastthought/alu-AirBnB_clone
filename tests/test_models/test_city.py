#!/usr/bin/python3
"""Unit tests for the City class."""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test cases for City."""

    DEFAULTS = {'state_id': '', 'name': ''}

    def test_inherits(self):
        """City inherits from BaseModel."""
        self.assertTrue(issubclass(City, BaseModel))

    def test_defaults(self):
        """Class attributes have the expected default values."""
        obj = City()
        for name, default in self.DEFAULTS.items():
            self.assertEqual(getattr(obj, name), default)

    def test_to_dict(self):
        """to_dict() reports the right class name."""
        self.assertEqual(City().to_dict()["__class__"], "City")

    def test_str(self):
        """__str__ starts with the class name."""
        self.assertTrue(str(City()).startswith("[City] ("))

    def test_from_dict(self):
        """City can be re-created from a dictionary."""
        obj = City()
        new = City(**obj.to_dict())
        self.assertEqual(obj.id, new.id)
        self.assertEqual(obj.created_at, new.created_at)

    def test_save(self):
        """save() updates updated_at."""
        obj = City()
        before = obj.updated_at
        obj.save()
        self.assertGreater(obj.updated_at, before)


if __name__ == "__main__":
    unittest.main()
