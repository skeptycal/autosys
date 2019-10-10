#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" as_pathlib.py """
# copyright (c) 2019 Michael Treanor
# https://www.github.com/skeptycal
# https://www.twitter.com/skeptycal

if True:
    import os
    import pathlib
    import sys
    import time
    from pathlib import WindowsPath, PosixPath, PurePath, Path
    from typing import Any, Dict, FrozenSet, List, Sequence, Tuple

if True:  # @autosys package modules
    # from . import *
    # from . import as_constants
    # from .as_constants import *
    # from . import as_time_it
    # from autosys.as_constants import PY_ENV, PY_BASE
    # from autosys.as_time_it import timeit
    # import autosys.as_time_it
    pass


timeit_results: List[float] = []


def timeit_init(arg: str = 'init') -> bool:
    global timeit_results
    if arg == 'init':
        timeit_results = []
    elif arg == 'log_on':


class TimeIt(list):
    log: bool = False

    def __init__(self, log_flag: bool = True, print_flag: bool = True):
        self.log_flag = log_flag
        self.print_flag = print_flag

    def reset():


def timeit(method):
    """
    Decorator - code timer for comparing and optimizing snippets
    """
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        timeit_results.append(te-ts)
        print("%r (%r, %r) %2.2f sec" % (method.__name__, args, kw, te - ts))
        return result

    return timed


def get_env_path() -> str:
    """ Return system path """
    return os.getenv('PATH')


class PPath(pathlib.PurePath):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __init__(self, path_name: pathlib.PurePath, args):
        if os.name == 'nt':
            Path = WindowsPath
        else:
            Path = PosixPath
        self.PP = path_name
        if SET_DEBUG:
            print(self.PP.as_uri())

    def subs(self):
        return [x for x in PP.iterdir() if x.is_dir()]

    def exists(self):
        return self.PP.exists()

    def is_dir(self):
        return self.PP.is_dir()

    def next_line(self):
        try:
            with self.PP.open() as f:
                return f.readline()
        except OSError as e:
            return e

    def name(self) -> str:
        return self.PP.parts()

    def str(self):
        return str(self.PP)

    def ls(self, args):
        for x in PP.iterdir():
            print(x)


def _get_builtins():
    return sys.builtin_module_names


def basename(filename: str) -> str:
    """
    get only basename from full path
    """
    try:
        # return Path(filename).resolve().parts()[-1]
        return Path(filename).resolve().name
    except OSError:
        return ''


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
    try:
        return '.'.join(str(i) for i in __import__('sys').version_info[:3])
    except OSError:
        return ''


def py_shell() -> str:
    """ Returns string containing current python shell name. """

    shell: str = "python"
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
        except ImportError:
            pass
        else:
            shell = platform.python_implementation()
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


def iterable(obj): return hasattr(
    obj, '__iter__') or hasattr(obj, '__getitem__')

# def njoin(l: List[str]) -> str:
#     return '\n'.join(l)


@timeit
def time_iter_check1(n: int = 10000, var: object = None):
    if not var:
        var = "*"*2000
    for _ in range(n):
        result = iterable(var)
    return result

# time_iter_check2 is xx% faster than time_iter_check1


@timeit
def time_iter_check2(n: int = 10000, var: object = None, i: int = 10) -> List[float]:
    if not var:
        var = "*"*2000

    for _ in range(n):
        try:
            result = iter(var)
            result = True
        except TypeError:
            result = False


def time_iter_check(n: int = 10000, var: object = None, i: int = 10) -> List[float]:
    results = []
    for _ in range(i):
        results.append(time_iter_check1(n, var))

        time_iter_check2(n, var)


def njoin(s, delimeter: str = ',') -> str:
    """
    Return a string of lines (with LF) from a delimited string or iterable object.
    """
    if isinstance(s, str):
        return '\n'.join(s.split(delimeter))
    try:
        _ = iter(s)
        return '\n'.join(_)
    except TypeError:
        pass


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

    print(njoin(_get_builtins()))
    print()
    print(njoin(get_env_path(), ':'))
    print(iterable('this'))
    print(iterable(5343))
    print(iterable([1, 2, 3, 4]))
    print(iterable(['a', 'b']))
    s1 = set(x for x in 'this')
    print(iterable(s1))
    print(iterable(pathlib.Path()))
    print(time_iter_check(1000000))
    print(basename(__doc__))
