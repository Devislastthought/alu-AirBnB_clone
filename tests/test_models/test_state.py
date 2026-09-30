#!/usr/bin/python3
"""Unit tests for the State class."""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test cases for State."""

    DEFAULTS = {'name': ''}

    def test_inherits(self):
        """State inherits from BaseModel."""
        self.assertTrue(issubclass(State, BaseModel))

    def test_defaults(self):
        """Class attributes have the expected default values."""
        obj = State()
        for name, default in self.DEFAULTS.items():
            self.assertEqual(getattr(obj, name), default)

    def test_to_dict(self):
        """to_dict() reports the right class name."""
        self.assertEqual(State().to_dict()["__class__"], "State")

    def test_str(self):
        """__str__ starts with the class name."""
        self.assertTrue(str(State()).startswith("[State] ("))

    def test_from_dict(self):
        """State can be re-created from a dictionary."""
        obj = State()
        new = State(**obj.to_dict())
        self.assertEqual(obj.id, new.id)
        self.assertEqual(obj.created_at, new.created_at)

    def test_save(self):
        """save() updates updated_at."""
        obj = State()
        before = obj.updated_at
        obj.save()
        self.assertGreater(obj.updated_at, before)


if __name__ == "__main__":
    unittest.main()
