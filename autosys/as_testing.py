# -*- coding: utf-8 -*-
"""
Testing Resources for autosys
"""
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


class TestException(Exception):
    """
    Exception handler override
    """

    # Reference: https://stackoverflow.com/questions/9823936/python-how-do-i-know-what-type-of-exception-occurred
    # template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    # message = template.format(type(ex).__name__, ex.args)
    # print message

    def __init__(self, parameter_list):
        Exception.__init__()


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


def get_v_name(the_var: Any) -> str:
    """
    Return string containing name of the_var
    """
    return [
        var_name for var_name, var_val
        in inspect.currentframe().f_back.f_locals.items()
        if var_val is the_var
    ][0]


def name_var(the_var: Any) -> List[str]:
    """
    Return tuple containing name and value of the_var
    """
    return [[
        var_name for var_name, var_val
        in inspect.currentframe().f_back.f_locals.items()
        if var_val is the_var][0], the_var]


def _add_dots(s: str,
              n: int,
              suffix: str = ' ...',
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


def print_var(
    the_string_name: str,
    the_string: str,
    p: int = DEFAULT_CLI_FIELD_PADDING,
    w: int = DEFAULT_CLI_DISPLAY_WIDTH,
    sep: str = DEFAULT_DICT_DISPLAY_SEPARATOR,
    print_it: bool = True
) -> str:
    """ Format string for 'var : value' pattern
        string_tuple: Tuple[str, str] - (name, value) of variable
        p: int - padding; len of name field
        w: int - width ; len of return string
        sep: str - separator
        print_it: bool - print to CLI within function
        """
    str_name = [var_name for var_name, var_val
                in inspect.currentframe().f_back.f_locals.items()
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


if __name__ == "__main__":

    if len(sys.argv) >= 2:
        filename = sys.argv[1]
    else:
        filename = 'example.py'

    print()
    print("Debug print values")
    print("*"*80)
    print()
    # print('_add_dots(name, 25, 15) : ', _add_dots(name, 25))
    # print('_add_dots(__name__, 25) : ', _add_dots(__name__, 25))
    # print('_add_dots(__file__, 45) : ', _add_dots(__file__, 45))
    # print('_add_dots(__version__, 15) : ', _add_dots(__version__, 15))
    # print('_add_dots(__package__, 25) : ', _add_dots(__package__, 25))
    print('v and name: ', name_var(__file__))
    print('get name - file: ', get_v_name(__file__))
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
    get_module_sig(inspect, )
