#!/usr/bin/python3
"""Unit tests for the FileStorage class."""
import os
import unittest
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage."""

    def setUp(self):
        """Start each test with empty storage and no file."""
        storage.all().clear()
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """Clean up after each test."""
        storage.all().clear()
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_instance(self):
        """storage is a FileStorage instance."""
        self.assertIsInstance(storage, FileStorage)

    def test_all_returns_dict(self):
        """all() returns a dictionary."""
        self.assertIsInstance(storage.all(), dict)

    def test_new(self):
        """new() stores objects under <class>.<id>."""
        obj = BaseModel()
        self.assertIn("BaseModel." + obj.id, storage.all())
        self.assertIs(storage.all()["BaseModel." + obj.id], obj)

    def test_save_creates_file(self):
        """save() writes the JSON file."""
        BaseModel().save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json") as f:
            self.assertIn("BaseModel.", f.read())

    def test_reload(self):
        """reload() restores saved objects of different classes."""
        base, user = BaseModel(), User()
        user.first_name = "Betty"
        base.save()
        storage.all().clear()
        storage.reload()
        self.assertIn("BaseModel." + base.id, storage.all())
        loaded = storage.all()["User." + user.id]
        self.assertIsInstance(loaded, User)
        self.assertEqual(loaded.first_name, "Betty")

    def test_reload_no_file(self):
        """reload() does nothing when the file is missing."""
        storage.reload()
        self.assertEqual(storage.all(), {})


if __name__ == "__main__":
    unittest.main()
