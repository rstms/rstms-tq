#!/usr/bin/env python3

try:
    from tomlib import loads
except ImportError:
    from tomli import loads

from json import dumps
from pathlib import Path
from subprocess import run
from sys import argv, exit, stdin
from tempfile import NamedTemporaryFile


def tq():
    args = ["jq"]
    script = None
    input_string = None
    for arg in argv[1:]:
        if arg.startswith("-"):
            args.append(arg)
        elif script is None:
            script = arg
            args.append(script)
        elif input_string is None:
            input_string = Path(arg).read_text()

    if input_string is None:
        input_string = stdin.read()

    data = loads(input_string)

    with NamedTemporaryFile() as tempfile:
        tempfile.write(dumps(data).encode())
        tempfile.seek(0)
        return run(args, stdin=tempfile).returncode


if __name__ == "__main__":
    exit(tq())
