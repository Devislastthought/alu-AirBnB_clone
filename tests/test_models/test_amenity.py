#!/usr/bin/python3
"""Unit tests for the Amenity class."""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity."""

    DEFAULTS = {'name': ''}

    def test_inherits(self):
        """Amenity inherits from BaseModel."""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_defaults(self):
        """Class attributes have the expected default values."""
        obj = Amenity()
        for name, default in self.DEFAULTS.items():
            self.assertEqual(getattr(obj, name), default)

    def test_to_dict(self):
        """to_dict() reports the right class name."""
        self.assertEqual(Amenity().to_dict()["__class__"], "Amenity")

    def test_str(self):
        """__str__ starts with the class name."""
        self.assertTrue(str(Amenity()).startswith("[Amenity] ("))

    def test_from_dict(self):
        """Amenity can be re-created from a dictionary."""
        obj = Amenity()
        new = Amenity(**obj.to_dict())
        self.assertEqual(obj.id, new.id)
        self.assertEqual(obj.created_at, new.created_at)

    def test_save(self):
        """save() updates updated_at."""
        obj = Amenity()
        before = obj.updated_at
        obj.save()
        self.assertGreater(obj.updated_at, before)


if __name__ == "__main__":
    unittest.main()
