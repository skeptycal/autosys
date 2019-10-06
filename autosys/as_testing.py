#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" as_testing.py """
# copyright (c) 2019 Michael Treanor
# https://www.github.com/skeptycal
# https://www.twitter.com/skeptycal

from __future__ import absolute_import

import importlib
import sys
import inspect
from typing import Any, Tuple, Dict, List

# Constants
DEFAULT_DICT_DISPLAY_SEPARATOR: str = ": "
DEFAULT_CLI_DISPLAY_WIDTH: int = 80
DEFAULT_CLI_FIELD_PADDING: int = 15
DEFAULT_CLI_FIELD_MIN_PADDING: int = 10

# class TestException(Exception):
# """
# Exception handler override
# """

# Reference: https://stackoverflow.com/questions/9823936/python-how-do-i-know-what-type-of-exception-occurred
# template = "An exception of type {0} occurred. Arguments:\n{1!r}"
# message = template.format(type(ex).__name__, ex.args)
# print message

# a = 1


def timeit(method):
    """
    Decorator - code timer for comparing and optimizing snippets
    """
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print("%r (%r, %r) %2.2f sec" % (method.__name__, args, kw, te - ts))
        return result

    return timed


def v_name(the_var: Any) -> str:
    """
    Return string containing name of the_var
    """
    try:
        result = [
            var_name for var_name, var_val in
            inspect.currentframe().f_back.f_locals.items()
            if var_val is the_var
        ][0]
        return result
    except IndexError as e:
        return ''


def name_var(the_var: Any) -> List[str]:
    """
    Return list containing name and value of the_var
    """
    return [[
        var_name for var_name, var_val in
        inspect.currentframe().f_back.f_locals.items() if var_val is the_var
    ][0], the_var]


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


def _add_dots(s: str, n: int, suffix: str = ' ...',
              add_dots: bool = True) -> str:
    """
    Truncate and return formatted string to fit <s> in <n> spaces
        add ' ...' if <add_dots> is True
    """
    str_len = n - len(suffix)
    if len(s) > str_len:
        s = s.ljust(str_len) + suffix
    return s


def get_module_sig(self, module, parameter_list):
    import inspect
    import example

    sig = inspect.signature(module)
    bound = sig.bind(
        'this is arg1',
        'this is arg2',
        'this is an extra positional argument',
        extra_named_arg='value',
    )
    print('Arguments:')

    for name, value in bound.arguments.items():
        print('{} = {!r}'.format(name, value))
    # for name, data in inspect.getmembers(example):
    #     if name.startswith('__'):
    #         continue
    #     print('{} : {!r}'.format(name, data))


def print_var(the_string_name: str,
              the_string: str,
              p: int = DEFAULT_CLI_FIELD_PADDING,
              w: int = DEFAULT_CLI_DISPLAY_WIDTH,
              sep: str = DEFAULT_DICT_DISPLAY_SEPARATOR,
              print_it: bool = True) -> str:
    """ Format string for 'var : value' pattern
        string_tuple: Tuple[str, str] - (name, value) of variable
        p: int - padding; len of name field
        w: int - width ; len of return string
        sep: str - separator
        print_it: bool - print to CLI within function
        """
    str_name = [
        var_name for var_name, var_val in
        inspect.currentframe().f_back.f_locals.items()
        if var_val is the_string_name
    ][0]
    print('str_name: ', str_name)
    result: str = ''
    if p == 0:
        p = len(the_string_name)
    if p <= DEFAULT_CLI_FIELD_MIN_PADDING:
        p = DEFAULT_CLI_FIELD_MIN_PADDING

    str_padding: int = w - p - len(sep)
    # print('p: ', p, ' str_p: ', str_padding)
    str_format: str = f'{{:<{p}.{p}}}{sep}{{:<{str_padding}.{str_padding}}}'
    print(str_format)
    # print(_add_dots(the_string, 16))
    # result = str_format.format(
    #     _add_dots(the_string_name, p), _add_dots(the_string, str_padding)
    # )
    if print_it:
        print(result)
    # print()
    # print("str_format: ", str_format)
    # print("result: ", result)
    # print()
    return result


def get_module_info(module: str):
    return 0
    # try:
    #     (name, suffix, mode, mtype) = inspect.getmoduleinfo(filename)
    # except TypeError:
    #     print('Could not determine module type of %s' % filename)
    # else:
    #     mtype_name = {imp.PY_SOURCE: 'source',
    #                   imp.PY_COMPILED: 'compiled',
    #                   }.get(mtype, mtype)

    #     mode_description = {'rb': '(read-binary)',
    #                         'U': '(universal newline)',
    #                         }.get(mode, '')

    #     print('NAME   :', name)
    #     print('SUFFIX :', suffix)
    #     print('MODE   :', mode, mode_description)
    #     print('MTYPE  :', mtype_name)


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


def _pprint_dict_table(data: Dict[Any, Any], name: str = "Data Table"):
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

    if len(sys.argv) >= 2:
        filename = sys.argv[1]
    else:
        filename = 'example.py'

    print()
    print("Debug print values")
    print("*" * 80)
    print()
    # print('_add_dots(name, 25, 15) : ', _add_dots(name, 25))
    # print('_add_dots(__name__, 25) : ', _add_dots(__name__, 25))
    # print('_add_dots(__file__, 45) : ', _add_dots(__file__, 45))
    # print('_add_dots(__version__, 15) : ', _add_dots(__version__, 15))
    # print('_add_dots(__package__, 25) : ', _add_dots(__package__, 25))
    print('v and name: ', name_var(__file__))
    print('get name - file: ', v_name(__file__))
    print("")
    # print_var()
    # print(locals())
    widths = [len(key) for key in list(locals().keys())]
    keys = [key for key in list(locals().keys())]
    padding = max(widths)
    # print(widths)
    # print()
    # print(keys)
    # for key in keys:
    #     # print(key, locals().get(key))
    #     print_var(key, locals().get(key))
    print()
    # get_module_sig(inspect, )
    # log = logging.getLogger()
    print(_run_tests())
    print()
    print("... Tests Complete.")
    _pprint_dict_table
