#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' as_system.py - system utilities and tools for efficient python3 '''
# copyright (c) 2019 Michael Treanor
# https://www.github.com/skeptycal
# https://www.twitter.com/skeptycal

SET_DEBUG: bool = False

if True:
    import os
    import pathlib
    import sys
    import time
    from pathlib import WindowsPath, PosixPath, PurePath, Path
    from typing import Any, Dict, FrozenSet, List, Sequence, Tuple


def _get_env_path():
    ''' Return system path '''
    return os.getenv('PATH')

def timeit(method):
    def timed(*args, **kw):
        s0 = sys.getsizeof(method)
        t0 = time.time()
        result = method(*args, **kw)
        dt = time.time() - t0
        s1 = sys.getsizeof(method)
        print(method.__name__)
        fn = var_name(kw.get('func'))
        # print(func_name)

        # if 'log_time' in kw:
        #     name = kw.get('log_name', method.__name__.upper())
        #     kw['log_time'][name] = int((dt) * 1000)
        # else:
        print(f"{fn:25.25} - {dt*1000:>6.6} \t{'ms':>3.2}")
        return result
    return timed

class PPath(pathlib.Path):
    ''' Base Path Object '''

    def __init__(self, pattern: pathlib.PurePath):
        self.pattern = pattern
        if SET_DEBUG:
            print(self.as_uri())
        super().__init__()

    def subs(self, recursive=False):
        """ Yield an iterator of subdirectories. """
        if recursive:
            func = self.rglob(self.pattern + '/')
        else:
            func = self.glob(self.pattern + '/')
        for _ in func:
            # if x.is_dir():
            yield _

    def exists(self):
        return self.exists()

    def is_dir(self):
        return self.is_dir()

    def next_line(self):
        try:
            with self.open() as f:
                return f.readline()
        except OSError as e:
            return e

    def get_name(self) -> str:
        return self.parts[0]

    def str(self):
        return str(self)

    def ls(self, args):
        for x in self.iterdir():
            print(x)


def _get_builtins() -> Sequence[str]:
    return sys.builtin_module_names


def _get_basename(filename: str) -> str:
    ''' get only basename from full path '''
    return Path(filename).resolve().parts()[-1]  # pathlib version
    # return os.path.basename(filename) # os.path version


def py_path() -> List[str]:
    ''' Return list of current python path elements. '''
    try:
        return os.environ['PYTHONPATH'].split(os.pathsep)
    except KeyError:
        return []


def py3up() -> bool:
    ''' Return True if 'Python >= 3' else False

        If you want to detect pre-Python 3 and don't want to import anything,
        you can (ab)use list comprehension scoping changes '''
    # https://stackoverflow.com/questions/1093322/how-do-i-check-what-version-of-python-is-running-my-script/35294211
    # https://stackoverflow.com/a/52825819/9878098
    return (lambda x: [x for x in [False]] and None or x)(True)


def pyver() -> str:
    ''' Returns string with python version number in major.minor.micro format.
            (e.g. 3.7.3  or  2.7.12) '''
    return '.'.join(str(i) for i in __import__('sys').version_info[:3])


def py_shell() -> str:
    ''' Returns string containing current python shell name.
            (e.g. ipython notebook, pypy, jupyter notebook, ipython, cpython) '''

    shell: str = "unknown"
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


def _pprint_globals():
    ''' Pretty Print all global variables.
        Designed for debugging purposes. '''
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


@timeit  # testing efficiency of version 1
def time_iter_check1(n: int = 10000, var: object = None):
    if not var:
        var = "*"*2000
    for _ in range(n):
        result = iterable(var)
    return result


@timeit  # testing efficiency of version 2
def time_iter_check2(n: int = 10000, var: object = None):
    if not var:
        var = "*"*2000

    for _ in range(n):
        try:
            result = iter(var)
            result = True
        except TypeError:
            result = False


def time_iter_check(n: int = 10000, var: object = None):
    time_iter_check1(n, var)
    time_iter_check2(n, var)


def njoin(s, delimeter: str = ',') -> str:
    ''' Return a string of lines (with LF) from a delimited string or iterable object. '''
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
    ''' Pretty Print dictionary in table format.
        parameters:
            data: Dict[Any, Any] - dictionary containing table data
            title: str - Displayed Title of Data Table (Title Case Used)
            borders: str - border format (single, double, graphic, text*) '''
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
            'print("basename: ", _get_basename(__file__))',
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
    print(njoin(_get_env_path(), ':'))
    print(iterable('this'))
    print(iterable(5343))
    print(iterable([1, 2, 3, 4]))
    print(iterable(['a', 'b']))
    s1 = set(x for x in 'this')
    print(iterable(s1))
    print(iterable(pathlib.Path()))
    print(time_iter_check(10000000))
