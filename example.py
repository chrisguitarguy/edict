#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import edict


def simple():
    """The simplest command, takes no arguments, has return annotation (default name)"""
    print('Hello, world')


def optionals(optional: "This is an optional argument"=None) -> "optionals":
    """Optional arguments turn into command line options"""
    print(optional)


def positionals(positional: "This is a positional, required argument") -> "positionals":
    """Positional arguments become command line arguments, and are required"""
    print(positional)


def store_false(is_true: "Uses the argparse action 'store_false'"=True) -> "store:true":
    """
    When arguments are set to True in the command function definition, their
    values will be set to false when the CLI flag is set
    """
    print(is_true)


def store_true(is_false: "Uses the argparse action 'store_true'"=False) -> "store:false":
    """
    When arguments are set to False in the command function definition, their
    values will be set to True when the CLI flag is set
    """
    print(is_false)


if __name__ == '__main__':
    app = edict.Application('Test Application', '1.0')
    app.add_command(simple)
    app.add_command(optionals)
    app.add_command(positionals)
    app.add_command(store_false)
    app.add_command(store_true)
    sys.exit(app.run())
