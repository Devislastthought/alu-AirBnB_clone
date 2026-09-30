#!/usr/bin/python3
"""Unit tests for the User class."""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for User."""

    DEFAULTS = {'email': '', 'password': '', 'first_name': '', 'last_name': ''}

    def test_inherits(self):
        """User inherits from BaseModel."""
        self.assertTrue(issubclass(User, BaseModel))

    def test_defaults(self):
        """Class attributes have the expected default values."""
        obj = User()
        for name, default in self.DEFAULTS.items():
            self.assertEqual(getattr(obj, name), default)

    def test_to_dict(self):
        """to_dict() reports the right class name."""
        self.assertEqual(User().to_dict()["__class__"], "User")

    def test_str(self):
        """__str__ starts with the class name."""
        self.assertTrue(str(User()).startswith("[User] ("))

    def test_from_dict(self):
        """User can be re-created from a dictionary."""
        obj = User()
        new = User(**obj.to_dict())
        self.assertEqual(obj.id, new.id)
        self.assertEqual(obj.created_at, new.created_at)

    def test_save(self):
        """save() updates updated_at."""
        obj = User()
        before = obj.updated_at
        obj.save()
        self.assertGreater(obj.updated_at, before)


if __name__ == "__main__":
    unittest.main()
