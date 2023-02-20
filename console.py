#!/usr/bin/python3
import cmd
form models.base_model import BaseModel


class HCommand(cmd.Cmd):
    prompt = '(hbnb)'

    """ Comandos básicos """
    def func_EOF(self, args):
        "EOF commando to exit the program\n"
        return True

    def func_quit(self, args):
        'Quit command to exit the program\n'

    def lineavacia(self):
        pass

HCommand().cmdloop()
