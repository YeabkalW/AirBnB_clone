#!/usr/bin/python3

"""Entry Point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """

    Command interpreter for the HBNB project
    """

    prompt = "(hbnb) "

    def do_quit(self):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """
        Exit on an EOF (end-of-file) character
        """

        return True

    def emptyline(self):
        """
        Handles empty line + Enter
        """
        pass

    if __name__ == '__main__':
        HBNBCommand().cmdloop()
