#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ps_sys.py - Basic os and system utilities for Python on macOS
"""


# the sys.path starts with the directory containing pysys.py which we want to remove as
# that dir might be anywhere and could contain anything; it's not needed for locating
# the pysys modules since those will be in site-packages once pysys is installed
from __future__ import absolute_import, print_function

import inspect
import locale
import logging
import os
import sys
import time
import traceback
from typing import Any, Dict, List

from pysystem import __main__
from version import __version__

script_path = os.path.abspath(sys.path[0])
sys.path = [p for p in sys.path if os.path.abspath(p) != script_path]

__main__.main()


# the sys.path starts with the directory containing pysys.py which we want to remove as
# that dir might be anywhere and could contain anything; it's not needed for locating
# the pysys modules since those will be in site-packages once pysys is installed


script_path = os.path.abspath(sys.path[0])
sys.path = [p for p in sys.path if os.path.abspath(p) != script_path]

__main__.main()


sys.path.insert(0, os.path.abspath("."))

##############################################
locale.setlocale(locale.LC_ALL, "")
CODE = locale.getpreferredencoding()


def basename(filename: str) -> str:
    """
    get only basename from full path
    # TODO translate to pathlib
    """
    return os.path.basename(filename)


def py_path() -> List:
    """
    Return list of current python path elements.
    """
    try:
        return os.environ["PYTHONPATH"].split(os.pathsep)
    except KeyError:
        return []


def py3up() -> bool:
    """
    Return True if 'Python >= 3' else False

    If you want to detect pre-Python 3 and don't want to import anything...
        you can (ab)use list comprehension scoping changes
    """
    # https://stackoverflow.com/questions/1093322/how-do-i-check-what-version-of-python-is-running-my-script/35294211
    # https://stackoverflow.com/a/52825819/9878098
    return (lambda x: [x for x in [False]] and None or x)(True)


def pyver() -> str:
    """
    Returns string with python version number
        in major.minor.micro format. (e.g. 3.7.3  or  2.7.12)
    """
    return ".".join(str(i) for i in __import__("sys").version_info[:3])


def py_shell() -> str:
    """
    Returns string containing current python shell name.
    """
    shell: str = ""
    PY_ENV = os.environ
    PY_BASE = os.path.basename(PY_ENV["_"])
    if "JPY_PARENT_PID" in PY_ENV:
        shell = "ipython notebook"
    elif "pypy" in PY_ENV:
        shell = "pypy"
    elif "jupyter-notebook" in PY_BASE:
        shell = "jupyter notebook"
    elif "ipython" in PY_BASE:
        shell = "ipython"
    else:
        try:
            import platform

            shell = platform.python_implementation()
        except ImportError:
            pass
    # print("pyshell() output: ", shell.strip())
    return shell.strip()


def lineno():
    """
    Returns the current line number in our program.
    """
    # Reference: http://code.activestate.com/recipes/145297-grabbing-the-current-line-number-easily/
    print(
        "line",
        inspect.getframeinfo(inspect.currentframe()).lineno,
        "of file",
        inspect.getframeinfo(inspect.currentframe()).filename,
    )
    return inspect.currentframe().f_back.f_lineno


def py_ls(path_name: str = ".") -> Exception:
    """
    List relative and absolute paths of files in <path_name>.
    Parameter: path_name: str
    Return: None for success or Exception
    """
    # Reference: https://developers.google.com/edu/python/utilities
    # Example pulls filenames from a dir, prints their relative and absolute paths

    try:
        filenames = os.listdir(path_name)
    except OSError as e:
        return e
    for filename in filenames:
        print(filename)  # foo.txt
        try:
            # dir/foo.txt (relative to current dir)
            print(os.path.join(dir, filename))
        except OSError as e:
            return e
        try:
            # /home/nick/dir/foo.txt
            print(os.path.abspath(os.path.join(dir, filename)))
        except OSError as e:
            return e
    return None


def _join(*values):
    """
    (ANSI encoding) Join a series of values with semicolons. The values
    are either integers or strings.
    """
    return ";".join(str(v) for v in values)


def _pprint_globals():
    """
    Pretty Print all global variables.
    Designed for debugging purposes.
    """
    print()
    print("Globals: ")
    print("*" * 40)
    width = max(len(i) for i in globals())
    print(width)
    for s in globals():
        print("{:<15.15} : {:<64.64}".format(s, str(globals().get(s))))
    print()
    test_list: List[int] = [1, 2, 3]
    test_list.append(4)
    test_list.append("five")


def _pprint_dict_table(data: Dict[Any], name: str = "Data Table"):
    """
    Pretty Print dictionary in table format.
    """
    print()
    print(name.title())
    print("*" * len(name))
    width = max(len(i) for i in data)
    print(width)
    for s in globals():
        print("{:<15.15} : {:<64.64}".format(s, str(globals().get(s))))
    print()
    test_list: List[int] = [1, 2, 3]
    test_list.append(4)
    test_list.append("five")


def _execute_test_code(tests: List[str]) -> List[Exception]:
    """
    Execute and report exceptions for code snippets.
    """
    result: List[Exception] = []
    for test in tests:
        try:
            # run test code
            print("=> ", test)
            exec(test)
        except Exception as e:
            result.append(e)
    return result


def _run_tests() -> str:
    """
    Run and report on specific tests for some functions in this module.
    """
    tests: List[str] = [
        "_pprint_globals()",
        'print("basename: ", basename(__file__))',
        "print(1/0)",
    ]

    for e in _execute_test_code(tests):
        # result = '\n'.join(str(e) for e in _execute_test_code(tests))
        # if result:
        #     print(result)
        # return result
        # print("traceback: ", traceback.format_exc())
        print("e.__class__.__name__", e.__class__.__name__)
        # log.exception(e)
        print("e: ", e)
        print("e.args: ", e.args)
        print("type(e): ", type(e))


def _pprint_code_tests(tests: List[Exception]):
    pass


if __name__ == "__main__":
    log = logging.getLogger()
    print(_run_tests())
    print()
    print("... Tests Complete.")
    _pprint_dict_table


# Parts of the setup and skeleton of pysystem were inspired by:
# PySys System Test Framework, Copyright (C) 2006-2019 M.B. Grieve

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.

# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
