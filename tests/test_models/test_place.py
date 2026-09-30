#!/usr/bin/python3
"""Unit tests for the Place class."""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test cases for Place."""

    DEFAULTS = {
        'city_id': '',
        'user_id': '',
        'name': '',
        'description': '',
        'number_rooms': 0,
        'number_bathrooms': 0,
        'max_guest': 0,
        'price_by_night': 0,
        'latitude': 0.0,
        'longitude': 0.0,
        'amenity_ids': [],
    }

    def test_inherits(self):
        """Place inherits from BaseModel."""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_defaults(self):
        """Class attributes have the expected default values."""
        obj = Place()
        for name, default in self.DEFAULTS.items():
            self.assertEqual(getattr(obj, name), default)

    def test_to_dict(self):
        """to_dict() reports the right class name."""
        self.assertEqual(Place().to_dict()["__class__"], "Place")

    def test_str(self):
        """__str__ starts with the class name."""
        self.assertTrue(str(Place()).startswith("[Place] ("))

    def test_from_dict(self):
        """Place can be re-created from a dictionary."""
        obj = Place()
        new = Place(**obj.to_dict())
        self.assertEqual(obj.id, new.id)
        self.assertEqual(obj.created_at, new.created_at)

    def test_save(self):
        """save() updates updated_at."""
        obj = Place()
        before = obj.updated_at
        obj.save()
        self.assertGreater(obj.updated_at, before)


if __name__ == "__main__":
    unittest.main()
