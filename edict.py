# -*- coding: utf-8 -*-
"""
edict
~~~~~

"""

import argparse
import inspect
import sys


class Application:
    """
    The central object of edict, this is used to define a new CLI application.

    .. versionadded:: 1.0
    """
    
    #: The application's name
    #: .. versionadded:: 1.0
    name = None

    #: The application's version
    #: .. versionadded:: 1.0
    version = None

    #: An argparse instance for the command
    #: .. versionadded:: 1.0
    parser = None

    #: The subparsers from argpass
    #: .. versionadded:: 1.0
    subparsers = None

    def __init__(self, name=None, version=None):
        self.name = name
        self.version = version
        self.parser = argparse.ArgumentParser(
                description=self.fullname,
                usage='%(prog)s [-h] {command} [options]'
            )
        self.parser.add_argument('--version', action='version', version=self.fullname)
        self.subparsers = self.parser.add_subparsers(title='Subcommands')

    @property
    def fullname(self):
        return '{name} ({ver})'.format(name=self.name or 'UNKNOWN', ver=self.version or 'UNKNOWN')

    def add_command(self, func):
        """
        Adds a new command to the application. The functions aruments are used
        to determine CLI arguments.
        """
        cmd = Command(func)
        parser = self.subparsers.add_parser(cmd.name, help=cmd.help)
        cmd.add_arguments(parser)
        parser.set_defaults(_command=cmd)

    def run(self, args=None):
        args = self.parser.parse_args(args)
        if '_command' not in args:
            self.parser.print_help();
            return 1
        return args._command.run(args)


class Command:

    func = None
    signature = None

    def __init__(self, func):
        self.func = func
        self.signature = inspect.signature(self.func)

    @property
    def name(self):
        if self.signature.return_annotation is self.signature.empty:
            return self.func.__name__
        return self.signature.return_annotation

    @property
    def help(self):
        return self.func.__doc__

    def add_arguments(self, parser):
        for _, param  in self.signature.parameters.items():
            self._add_argument(parser, param)

    def run(self, args):
        run_args = dict()
        for name, param in self.signature.parameters.items():
            run_args[name] = getattr(args, name)
        bound = self.signature.bind(**run_args)
        return self.func(*bound.args, **bound.kwargs)

    def _add_argument(self, parser, param):
        name = param.name if param.default is param.empty else '--{opt}'.format(opt=param.name)
        definition = dict()

        definition['action'] = 'store'
        if param.default is True:
            definition['action'] = 'store_false'
        elif param.default is False:
            definition['action'] = 'store_true'
        elif param.default is not param.empty:
            definition['default'] = param.default

        if param.kind is param.VAR_POSITIONAL:
            definition['nargs'] = '*'

        if param.annotation is not param.empty:
            definition['help'] = param.annotation

        parser.add_argument(name, **definition)

    def __repr__(self):
        return '<Command={name}>'.format(name=self.name)
