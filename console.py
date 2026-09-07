#!/usr/bin/python3
"""The simple command interpreter for the AirBnB clone."""

import cmd
import shlex

from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Accept commands for creating and managing model objects."""

    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }

    def do_quit(self, line):
        """Quit the program."""
        return True

    def do_EOF(self, line):
        """Quit when the user presses Ctrl-D."""
        print()
        return True

    def emptyline(self):
        """Do nothing when the user enters a blank line."""
        pass

    def do_create(self, line):
        """Create a model: create User."""
        words = shlex.split(line)
        if not words:
            print("** class name missing **")
            return
        if words[0] not in self.classes:
            print("** class doesn't exist **")
            return
        print(self.classes[words[0]]().id)

    def do_show(self, line):
        """Show one model: show User id."""
        words = shlex.split(line)
        if not words:
            print("** class name missing **")
        elif words[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(words) < 2:
            print("** instance id missing **")
        else:
            obj = storage.all().get("{}.{}".format(words[0], words[1]))
            print(obj if obj else "** no instance found **")

    def do_destroy(self, line):
        """Delete one model: destroy User id."""
        words = shlex.split(line)
        if not words:
            print("** class name missing **")
        elif words[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(words) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(words[0], words[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, line):
        """List objects: all or all User."""
        words = shlex.split(line)
        if words and words[0] not in self.classes:
            print("** class doesn't exist **")
            return
        objects = storage.all().values()
        if words:
            objects = [obj for obj in objects
                       if obj.__class__.__name__ == words[0]]
        print([str(obj) for obj in objects])

    def do_update(self, line):
        """Update a model: update User id name value."""
        words = shlex.split(line)
        if not words:
            print("** class name missing **")
        elif words[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(words) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(words[0], words[1]) not in storage.all():
            print("** no instance found **")
        elif len(words) < 3:
            print("** attribute name missing **")
        elif len(words) < 4:
            print("** value missing **")
        else:
            obj = storage.all()["{}.{}".format(words[0], words[1])]
            value = words[3]
            if value.replace(".", "", 1).isdigit():
                value = float(value) if "." in value else int(value)
            setattr(obj, words[2], value)
            obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
