#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
autosys_system.py
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
SIN: Dict[float, float] = {a: math.sin(a) for a in range(360)}


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
