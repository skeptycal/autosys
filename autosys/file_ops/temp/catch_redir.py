#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 'Standard Library'
import locale
import sys

from os import linesep as NL
from pathlib import Path
from subprocess import check_output
from sys import argv, platform

from typing import Dict, List, Sequence

# ---------------------- utility functions


def br(n: int = 1, retval: bool = False):
    """ #### Prints a blank line using the OS specific line
        separator from `os.linesep`.

        Yes, it is just a shorter pythonic version of

        `<br />`
        """
    if retval:
        return NL * n
    print(NL * n, sep="", end="")


def j(s: Sequence, sep=", ") -> str:
    """ #### Returns string of joined sequence items.

        Yes, it is just a shorter version of

        `', '.join(sequence)`
        """
    return sep.join(s)


class ConfigVars(dict):
    """ Configuration information and variable defaults """

    _DEBUG_: bool = False
    WIN32: bool = platform.startswith("windows")
    WIDTH: int = 57
    ARGS: List[str] = argv[1:]
    ENCODING: str = ""
    _output_filename: str = "badfile.txt"

    def __init__(self):
        super().__init__(self)
        try:
            self.ENCODING = locale.getpreferredencoding()
        except locale.Error as e:
            self.ENCODING = "utf-8"  # set default on locale errors

    def dir_commands(self) -> List[str]:
        """ Return sample directory listing shell command. """
        return ["dir", "*.*"] if self.WIN32 else ["ls", "-l", "."]

    def output_path(self) -> str:
        p = Path("C:/temp") if self.WIN32 else Path().home()
        p /= "temp"
        p /= self._output_filename
        return str(p)

    def test_config(self, *args):
        """ List debug info. """
        if self._DEBUG_:
            dunders = sorted([_ for _ in dir(self) if _.startswith("__")])

            dirs = sorted([_ for _ in dir(self) if not _.startswith("__")])

            _vars = [s for s in dirs if s.startswith("_")]
            lowers = [s for s in dirs if s.islower()]
            uppers = [s for s in dirs if s.isupper()]

            br()
            print("Debug Info:")
            print("-" * self.WIDTH)

            print(f"CONSTANTS: {uppers}")
            for var in uppers:
                val = eval(f"self.{var}")
                print(f"   {var:12.12} = {val}")

            br()
            print(f"properties and methods: \n\t{lowers}")
            br()
            # print(f"dunders: \n\t{dunders}")
            # br()
            print(f"{self.output_path()=}")
            print("-" * self.WIDTH)
            br()


def check_args(*args):
    """ Respond to CLI arguments. """
    pass


def log_cmd(*args) -> int:
    """ Log shell commands to a file.

        Parameters:
            c: a ConfigVars object with variables, data, and utilities

        Returns:
            int -- error code; 0 for success

        One-liner:
            with open('C:/temp/badfile.txt', mode='at',) as f:
                f.write(subprocess.check_output(['dir','*.*']).decode())
        """

    try:
        retval = check_output(c.dir_commands()).decode()
        if c._DEBUG_:
            print(f"function return value:\n\n{retval}")
    except Exception as e:
        print(f"Error processing command: {j(c.dir_commands(),sep=' ')}")
        print(e)
    with open(c.output_path(), mode="at",) as f:
        try:
            if c._DEBUG_:
                print("Debug Info for Output File System:")
                print(f"   {sys.byteorder=}")
                print(f"   {sys.api_version=}")
                print(f"   {f.fileno()=}")
                print(f"   {f.isatty()=}")
                print(f"   {f.seekable()=}")
                print(f"   {f.writable()=}")
            f.write(retval)
        except Exception as e:
            print(f"Error writing to file: {c.output_path()}")
            print(e)


def main(*args):
    """
    CLI script main entry point.
    """
    check_args(c)  # do more stuff with args
    c.test_config()
    retval = log_cmd()
    if retval:
        print("Errors occurred with the command logging.")


if __name__ == "__main__":  # if script is loaded directly from CLI
    c = ConfigVars()
    # c._DEBUG_ = True # comment out this line to turn off DEBUG output

    main(c)
