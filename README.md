# Edict

Edict is a library for creating CLI applications in Python (3.3+). It uses
function annotations to build help text.

## Installation (Comming Soon?)

    shell> pip install edict

## Quickstart

```python
import sys
import edict

def some_command(argument_one: "This is help text for the argument") -> "command_name"
    """The docblock of the command will be used as help text of the command"""
    # do stuff

if __name__ == '__main__'
    cli = edict.Application()
    cli.add_command(some_command)
    sys.exit(cli.run())
```
