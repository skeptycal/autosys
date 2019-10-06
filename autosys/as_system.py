#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" as_system.py """
# copyright (c) 2019 Michael Treanor
# https://www.github.com/skeptycal
# https://www.twitter.com/skeptycal

# from __future__ import absolute_import, print_function
# from typing import Any, Dict, FrozenSet, List, Sequence, Tuple
from autosys import *


def _get_builtins():
    return sys.builtin_module_names


def basename(filename: str) -> str:
    """
    get only basename from full path
    # TODO translate to pathlib
    """
    return os.path.basename(filename)


def py_path() -> List[str]:
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
    print(f'(key width: {width})')
    for s in globals():
        print("{:<15.15} : {:<64.64}".format(s, str(globals().get(s))))
    print()


def njoin(l: List[str]) -> str:
    return '\n'.join(l)


def _pprint_code_tests(tests: List[Exception]):
    pass


def _get_functions():
    pass


def _pprint_dict_table(data: Dict[Any, Any] = globals(),
                       title: str = "",
                       borders: str = 'text'):
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

    fmt = ("{:<" + str(width) + "." + str(width) + "} : " + "{:<" +
           str(width2) + "." + str(width2) + "}")

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


if __name__ == "__main__":
    # log = logging.getLogger()
    print(_run_tests())
    print()
    print("... Tests Complete.")
    _pprint_dict_table

    print(_get_builtins)
