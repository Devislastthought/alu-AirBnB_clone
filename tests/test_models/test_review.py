#!/usr/bin/python3
"""Unit tests for the Review class."""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test cases for Review."""

    DEFAULTS = {'place_id': '', 'user_id': '', 'text': ''}

    def test_inherits(self):
        """Review inherits from BaseModel."""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_defaults(self):
        """Class attributes have the expected default values."""
        obj = Review()
        for name, default in self.DEFAULTS.items():
            self.assertEqual(getattr(obj, name), default)

    def test_to_dict(self):
        """to_dict() reports the right class name."""
        self.assertEqual(Review().to_dict()["__class__"], "Review")

    def test_str(self):
        """__str__ starts with the class name."""
        self.assertTrue(str(Review()).startswith("[Review] ("))

    def test_from_dict(self):
        """Review can be re-created from a dictionary."""
        obj = Review()
        new = Review(**obj.to_dict())
        self.assertEqual(obj.id, new.id)
        self.assertEqual(obj.created_at, new.created_at)

    def test_save(self):
        """save() updates updated_at."""
        obj = Review()
        before = obj.updated_at
        obj.save()
        self.assertGreater(obj.updated_at, before)


if __name__ == "__main__":
    unittest.main()
