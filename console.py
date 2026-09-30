#!/usr/bin/python3
"""Entry point of the AirBnB clone command interpreter."""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter to manage AirBnB objects."""

    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel, "User": User, "State": State,
               "City": City, "Amenity": Amenity, "Place": Place,
               "Review": Review}

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """EOF signal (Ctrl+D) to exit the program
        """
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    @staticmethod
    def _split(arg):
        """Split arg into words, keeping double-quoted strings together."""
        try:
            return shlex.split(arg)
        except ValueError:
            return arg.split()

    def _check(self, arg, need_id=True):
        """Validate class name and id; print errors and return args."""
        args = self._split(arg)
        if not args:
            print("** class name missing **")
            return None
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return None
        if not need_id:
            return args
        if len(args) < 2:
            print("** instance id missing **")
            return None
        if "{}.{}".format(args[0], args[1]) not in storage.all():
            print("** no instance found **")
            return None
        return args

    def do_create(self, arg):
        """Create a new instance, save it and print its id
        Usage: create <class name>
        """
        args = self._check(arg, need_id=False)
        if args is None:
            return
        obj = self.classes[args[0]]()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Print the string representation of an instance
        Usage: show <class name> <id>
        """
        args = self._check(arg)
        if args is None:
            return
        print(storage.all()["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """Delete an instance and save the change
        Usage: destroy <class name> <id>
        """
        args = self._check(arg)
        if args is None:
            return
        del storage.all()["{}.{}".format(args[0], args[1])]
        storage.save()

    def do_all(self, arg):
        """Print all instances, optionally filtered by class name
        Usage: all [<class name>]
        """
        args = self._split(arg)
        if args and args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        print([str(obj) for obj in storage.all().values()
               if not args or obj.__class__.__name__ == args[0]])

    @staticmethod
    def _cast(obj, name, value):
        """Cast value to the type of the existing attribute if numeric."""
        current = getattr(obj, name, None)
        if type(current) in (int, float):
            try:
                return type(current)(value)
            except ValueError:
                return value
        return value

    def do_update(self, arg):
        """Update an instance attribute and save the change
        Usage: update <class name> <id> <attribute name> "<value>"
        """
        args = self._check(arg)
        if args is None:
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = storage.all()["{}.{}".format(args[0], args[1])]
        setattr(obj, args[2], self._cast(obj, args[2], args[3]))
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
