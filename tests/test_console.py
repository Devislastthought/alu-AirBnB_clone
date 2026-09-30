#!/usr/bin/python3
"""Unit tests for the console."""
import io
import os
import unittest
from unittest.mock import patch
from console import HBNBCommand
from models import storage


class TestConsole(unittest.TestCase):
    """Test cases for HBNBCommand."""

    def setUp(self):
        """Start each test with empty storage."""
        storage.all().clear()
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """Clean up after each test."""
        self.setUp()

    @staticmethod
    def run_cmd(line):
        """Run a console command and return what it printed."""
        with patch("sys.stdout", new=io.StringIO()) as out:
            HBNBCommand().onecmd(line)
        return out.getvalue().strip()

    def test_quit_and_empty(self):
        """quit returns True; an empty line prints nothing."""
        self.assertTrue(HBNBCommand().onecmd("quit"))
        self.assertEqual(self.run_cmd(""), "")

    def test_errors(self):
        """Error messages follow the specification."""
        self.assertEqual(self.run_cmd("create"), "** class name missing **")
        self.assertEqual(self.run_cmd("create Foo"),
                         "** class doesn't exist **")
        self.assertEqual(self.run_cmd("show BaseModel"),
                         "** instance id missing **")
        self.assertEqual(self.run_cmd("show BaseModel 1"),
                         "** no instance found **")
        self.assertEqual(self.run_cmd("all Foo"), "** class doesn't exist **")
        self.assertEqual(self.run_cmd("update BaseModel"),
                         "** instance id missing **")

    def test_create_show_destroy(self):
        """create, show and destroy work together."""
        for name in HBNBCommand.classes:
            uid = self.run_cmd("create " + name)
            self.assertIn(uid, self.run_cmd("show {} {}".format(name, uid)))
            self.run_cmd("destroy {} {}".format(name, uid))
            self.assertEqual(self.run_cmd("show {} {}".format(name, uid)),
                             "** no instance found **")

    def test_all(self):
        """all lists strings, filtered by class when asked."""
        self.run_cmd("create User")
        self.run_cmd("create State")
        self.assertEqual(self.run_cmd("all User").count("[User]"), 1)
        self.assertEqual(self.run_cmd("all").count(") {"), 2)

    def test_update(self):
        """update sets and casts attributes."""
        uid = self.run_cmd("create Place")
        base = "update Place {} ".format(uid)
        self.assertEqual(self.run_cmd(base), "** attribute name missing **")
        self.assertEqual(self.run_cmd(base + "name"), "** value missing **")
        self.run_cmd(base + 'name "My little house"')
        self.run_cmd(base + "max_guest 4")
        self.run_cmd(base + "latitude 37.7")
        obj = storage.all()["Place." + uid]
        self.assertEqual(obj.name, "My little house")
        self.assertEqual(obj.max_guest, 4)
        self.assertEqual(obj.latitude, 37.7)


if __name__ == "__main__":
    unittest.main()
