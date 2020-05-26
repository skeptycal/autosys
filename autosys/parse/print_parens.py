#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Add parentheses around print arguments.

    Used in translating Python 2 code modules to Python 3.

    https://pymotw.com/2/traceback/index.html#module-traceback
    The examples below use the module traceback_example.py (provided in the source package for PyMOTW). The contents are:
    """

import re
import sys
import traceback

"""
Add parens around print arguments
VS Code regex replacement for print function:
    print ([']{1}.*)\n
    print($1)\n
"""

FIND_PARENTS: re.Pattern = re.compile(r"([']{1}.*)\n")


def fix_parens(filenames):
    for file in filenames:
        with open(file, mode="r") as f:
            for line in f.readlines():
                fp = re.Pattern.sub()


if __name__ == "__main__":
    _debug_: bool = True  # True => use Debug features
    _verbose_: int = 0  # Verbosity level => 0 - 4
    _log_flag_: bool = _debug_ and True  # True => log to file if _debug_
    # argv.append('version')  # ! test
    # argv.append('help')  # ! test
    fix_parens(sys.argv[1:])
