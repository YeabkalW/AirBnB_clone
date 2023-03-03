#!/usr/bin/python3

"""
defines a class that contains the entry point
of the command interpreter.
"""

import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """
    defines the entry point for
    the command interpreter.
    """

    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    classes = {
                'BaseModel': BaseModel, 'User': User, 'Place': Place,
                'State': State, 'City': City, 'Amenity': Amenity,
                'Review': Review
              }

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def help_quit(self):
        """
        Prints help text for quit command
        """
        print('Quit command to exit the program\n')

    def do_EOF(self, line):
        """
        Quit command to exit the program
        """
        return True

    def help_EOF(self):
        """
        prints the help documentation for EOF
        """
        print('Quit command to exit the program')

    def emptyline(self):
        """
        Stops empty line form executing anything
        """
        pass

    def do_create(self, line):
        """
        Creates new instance of BaseModel
        Then saves it to a JSON file

        Prints:
            The object id
        """
        if not line:
            print("** class name missing **")
            return
        elif line not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            new_instance = self.classes[line]()
            storage.save()
            print(new_instance.id)

    def help_create(self):
        """
        defines the help message for create
        """

        print('Creates a new instance of any class\n'
              'that is in the program')
        print('[Usage] - (hbnb) create <Class Name>')

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on its class new and id.
        """

        # separating line args
        list_args = line.split(" ")

        arg1 = list_args[0]
        arg2 = list_args[1]

        if not arg1:
            print("** class name missing **")
            return
        elif arg1 not in self.classes:
            print("** class doesn't exist **")
            return
        elif arg1 and not arg2:
            print("** instance id missing **")
            return
        else:

            key = arg1 + "." + arg2
            try:
                print(storage._FileStorage__objects[key])
            except KeyError:
                print("** no instance found **")

    def help_show(self):
        """
        defines help message for (show)
        """
        print("Shows an individual instance of a class")
        print("[usage]: show <class name> <object id>\n")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        and saves the change to a JSON FILE
        """

        list_args = line.split(" ")
        arg1 = list_args[0]
        arg2 = list_args[1]

        if not arg1:
            print("** class name missing **")
            return
        elif arg1 not in self.classes:
            print("** class doesn't exist **")
            return
        elif arg1 and not arg2:
            print("** instance id is missing **")
            return
        else:

            key = arg1 + "." + arg2

            try:
                del (storage.all()[key])
                storage.save()
            except KeyError:
                print("** no instance found **")

    def help_destroy(self):
        """
        defines help message for (destroy)
        """

        print("Deletes an instance based on the class name and id")
        print("[Usage]: destroy <class name> <instance id>\n")

    def do_all(self, line):
        """
        prints all string representation of all instances of a class
        based or not on the class name
        """
        # creating an empty list
        list = []

        if line:
            line = line.split(' ')[0]
            if line not in self.classes:
                print("** class doesn't exist **")
                return
            for key, value in storage._FileStorage__objects.items():
                if key.split(".")[0] == line:
                    list.append(str(value))
        else:
            for key, value in storage._FileStorage__objects.items():
                list.append(str(value))

        print(list)

    def help_all(self):
        """
        Defines help message for (all)
        """

        print("prints all string representation of all instances of a class"
              "based or not on the class name")
        print("[Usage]: all <class name> or all\n")

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        """

        list = line.split(" ")
        arg1 = list[0]
        arg2 = list[1]
        arg3 = list[2]
        arg4 = list[3]

        key = arg1 + "." + arg2

        if not arg1:
            print("** class name missing **")
            return

        elif arg1 not in self.classes:
            print("** class doesn't exist **")
            return

        elif not arg2:
            print("** instance id missing **")
            return

        elif arg1 + "." + arg2 not in storage._FileStorage__objects.keys():
            print("** no instance found **")
            return

        elif not arg3:
            print("** attribute name missing **")
            return

        elif not arg4:
            print("** value missing **")
            return

        else:
            update = storage._FileStorage__objects[key]
            update.arg3 = arg4

    def help_update(self):
        """
        Defines help message for (update)
        """

        print("Updates an instance based on the class name"
              "and id by adding or updating attribute")
        print("[Usage]: update <class name> <id> <attribute name>"
              "<attribute value>\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
