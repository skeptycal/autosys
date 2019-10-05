#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
as_system.py
"""
from __future__ import absolute_import, print_function

if True:  # imports
    import fileinput
    import locale
    import math
    import os
    import sys
    import textwrap
    import timeit

if True:
    from typing import List, Dict, Tuple, Any
    from autosys import __version__ as version
    from autosys import name

# * @AUTOSYS_PARSE: START
##############################################
# Environment
SET_DEBUG: bool = True

locale.setlocale(locale.LC_ALL, "")
DEFAULT_LANG: str = locale.getlocale()[0] if locale.getlocale()[0] else "en_US"
DEFAULT_ENCODING: str = locale.getlocale()[1] if locale.getlocale()[
    1] else "UTF-8"
PREFERRED_ENCODING: str = locale.getpreferredencoding()
PY3: bool = (lambda x: [x for x in [False]] and None or x)(True)
_PY2 = sys.version_info[0] == 2
PY_VER: str = ".".join(str(_) for _ in __import__("sys").version_info[:3])
PY_ENV: Dict[str, str] = os.environ
PYTHON_PATH = PY_ENV["PYTHONPATH"].split(os.pathsep)
PY_BASE = os.path.basename(PY_ENV["_"])

##############################################
# DEFAULT CONSTANTS
DEFAULT_DICT_DISPLAY_SEPARATOR: str = ": "
DEFAULT_CLI_DISPLAY_WIDTH: int = 80
DEFAULT_CLI_FIELD_PADDING: int = 15

##############################################
# working variables
file_list: List[str] = []
i: int = 0
n: int = 0
filename: str = ""
word_list: List[str] = []

##############################################
# math functions
# example lookup table
SIN: Dict[float, float] = {a: math.sin(a/10) for a in range(3600)}


##############################################
class C_ERRORS:
    """
    C++ style error messages
        Reference:
        Advanced Bash-Scripting Guide
        <http://tldp.org/LDP/abs/html/exitcodes.html#EXITCODESREF>
        from /usr/include/sysexits.h
        Copyright (c) 1987, 1993
        The Regents of the University of California.  All rights reserved.
    """
    EX_OK = 0,          # successful termination
    EX__BASE = 64,      # base value for error messages
    EX_USAGE = 64,      # command line usage error
    EX_DATAERR = 65,    # data format error
    EX_NOINPUT = 66,    # cannot open input
    EX_NOUSER = 67,     # addressee unknown
    EX_NOHOST = 68,     # host name unknown
    EX_UNAVAILABL = 69,  # service unavailable
    EX_SOFTWARE = 70,   # internal software error
    EX_OSERR = 71,      # system error (e.g., can't fork)
    EX_OSFILE = 72,     # critical OS file missing
    EX_CANTCREAT = 73,  # can't create (user) output file
    EX_IOERR = 74,      # input/output error
    EX_TEMPFAIL = 75,   # temp failure; user is invited to retry
    EX_PROTOCOL = 76,   # remote error in protocol
    EX_NOPERM = 77,     # permission denied
    EX_CONFIG = 78,     # configuration error
    EX__MAX = 78        # maximum listed value


# * @AUTOSYS_PARSE: STOP
if __name__ == "__main__":
    print()
    print("PY_ENV: ", PY_ENV.get("CANARY"))
    print("Test Values")
    print("*" * 40)
    print("PY_ENV: ", PY_ENV.get("RESET_FG"))
    print("name: ", name)
    print("version: ", version)
    print("DEFAULT_ENCODING: ", DEFAULT_ENCODING)
    print("python version 3+: ", PY3)
    print("PY_VER: ", PY_VER)
    print("PY_BASE: ", PY_BASE)
    print("SIN: ", SIN.get(75))
    print("PYTHON_PATH: ", PYTHON_PATH)

    print()
    print("__doc__", __doc__)
    print("__file__", __file__)
    print("__package__", __package__)
    print("__name__", __name__)
