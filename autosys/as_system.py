#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
autosys_system.py
"""
from __future__ import absolute_import, print_function

import autosys
import inspect
import locale
import logging
import os
import sys
import time
import traceback
from typing import Any, Dict, List


# sys.path.insert(0, os.path.abspath("."))


# ##############################################
# SET_DEBUG: bool = True
# locale.setlocale(locale.LC_ALL, "")
# DEFAULT_ENCODING = locale.getpreferredencoding()


class BorderType():
    types: str = {'single', 'double', 'graphic', 'text'}


class TestException(Exception):

    # Reference: https://stackoverflow.com/questions/9823936/python-how-do-i-know-what-type-of-exception-occurred
    # template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    # message = template.format(type(ex).__name__, ex.args)
    # print message

    def __init__(self, parameter_list):
        Exception.__init__()


def _get_builtins(): return sys.builtin_module_names


def basename(filename: str) -> str:
    """
    get only basename from full path
    # TODO translate to pathlib
    """
    return os.path.basename(filename)


def py_path() -> List:
    """ Return list of current python path elements. """
    try:
        return os.environ['PYTHONPATH'].split(os.pathsep)
    except KeyError:
        return []


def py3up() -> bool:
    """ Return True if 'Python >= 3' else False

        If you want to detect pre-Python 3 and don't want to import anything...
        ... you can (ab)use list comprehension scoping changes
    """
    # https://stackoverflow.com/questions/1093322/how-do-i-check-what-version-of-python-is-running-my-script/35294211
    # https://stackoverflow.com/a/52825819/9878098
    return (lambda x: [x for x in [False]] and None or x)(True)


def pyver() -> str:
    """ Returns string with python version number in major.minor.micro format.
            (e.g. 3.7.3  or  2.7.12)
    """
    return '.'.join(str(i) for i in __import__('sys').version_info[:3])


def py_shell() -> str:
    """ Returns string containing current python shell name. """

    shell: str = ""
    # PY_ENV = os.environ
    # PY_BASE = os.path.basename(PY_ENV["_"])
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


def _pprint_dict_table(
    data: Dict[Any, Any] = globals(), title: str = "", borders: border_type = "text"
):
    """
    Pretty Print dictionary in table format.
    parameters:
        data: Dict[Any, Any] - dictionary containing table data
        title: str - Displayed Title of Data Table (Title Case Used)
        borders: str - border format (single, double, graphic, text*)
    """
    if title == "":
        title = data.__repr__()
    print(data.__repr__())
    print(data.__str__())
    maxwidth: int = 75  # 80 - 1 for each outer border and 3 for center padding
    width: int = max(len(i) for i in data) + 1
    width2: int = maxwidth - width
    if SET_DEBUG:
        print()
        print("Title: ", title.title())
        print("*" * len(title))
        print("width: ", width)
        print("width2: ", width2)

    fmt = (
        "{:<"
        + str(width)
        + "."
        + str(width)
        + "} : "
        + "{:<"
        + str(width2)
        + "."
        + str(width2)
        + "}"
    )

    print("*" * 80)
    for s in globals():
        print(fmt.format(s, str(globals().get(s))))
    print("*" * 80)


def _execute_test_code(tests: List[str]) -> List[Exception]:
    result: List[Exception] = []
    for test in tests:
        try:
            # run test code
            print("=> ", test)
            exec(test)
        except Exception as e:
            result.append(e)
    return result


def _run_tests(tests: List[str] = []) -> str:
    if tests == []:
        tests: List[str] = [
            "_pprint_globals()",
            'print("basename: ", basename(__file__))',
            "print(1/0)",
        ]

    results = _execute_test_code(tests)
    for e in results:
        print("e.__class__.__name__", e.__class__.__name__)
        # log.exception(e)
        print("e: ", e)
        print("e.args: ", e.args)
        print("type(e): ", type(e))


def _pprint_code_tests(tests: List[Exception]):
    pass


def _get_functions():
    pass


if __name__ == "__main__":
    log = logging.getLogger()
    print(_run_tests())
    print()
    print("... Tests Complete.")
    _pprint_dict_table

    print(_get_builtins)


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pysystem.py - System utilities for Python on macOS
"""

# the sys.path starts with the directory containing pysys.py which we want to remove as
# that dir might be anywhere and could contain anything; it's not needed for locating
# the pysys modules since those will be in site-packages once pysys is installed


script_path = os.path.abspath(sys.path[0])
sys.path = [p for p in sys.path if os.path.abspath(p) != script_path]

sys.path.insert(0, os.path.abspath("."))  # insert pwd

##############################################
locale.setlocale(locale.LC_ALL, "")
CODE = locale.getpreferredencoding()


if __name__ == "__main__":
    pass
    # log = logging.getLogger()
    # print(_run_tests())
    # print()
    # print("... Tests Complete.")
    # _pprint_dict_table

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


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
syspy.py
"""


sys.path.insert(0, os.path.abspath("."))

##############################################
locale.setlocale(locale.LC_ALL, "")
CODE = locale.getpreferredencoding()


class TestException(Exception):

    # Reference: https://stackoverflow.com/questions/9823936/python-how-do-i-know-what-type-of-exception-occurred
    # template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    # message = template.format(type(ex).__name__, ex.args)
    # print message

    def __init__(self, parameter_list):
        Exception.__init__()


def basename(filename: str) -> str:
    """
    get only basename from full path
    # TODO translate to pathlib
    """
    return os.path.basename(filename)


def py_path() -> List:
    """ Return list of current python path elements. """
    try:
        return os.environ["PYTHONPATH"].split(os.pathsep)
    except KeyError:
        return []


def py3up() -> bool:
    """ Return True if 'Python >= 3' else False

        If you want to detect pre-Python 3 and don't want to import anything...
        ... you can (ab)use list comprehension scoping changes
    """
    # https://stackoverflow.com/questions/1093322/how-do-i-check-what-version-of-python-is-running-my-script/35294211
    # https://stackoverflow.com/a/52825819/9878098
    return (lambda x: [x for x in [False]] and None or x)(True)


def pyver() -> str:
    """ Returns string with python version number in major.minor.micro format.
            (e.g. 3.7.3  or  2.7.12)
    """
    return ".".join(str(i) for i in __import__("sys").version_info[:3])


def py_shell() -> str:
    """ Returns string containing current python shell name. """

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
    tests: List[str] = [
        "_pprint_globals()",
        'print("basename: ", basename(__file__))',
        "print(1/0)",
    ]
    _execute_test_code(tests)
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
