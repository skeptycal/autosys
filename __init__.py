# -*- coding: utf-8 -*-
from __future__ import absolute_import

import inspect
# from dataclasses import dataclass
from typing import Any, Tuple

# TODO setup a way to automatically track semvers
__version__ = "1.0.2"

# set default package name to parent folder name
name = __file__.split("/")[-2]
__package__ = name

# Constants
DEFAULT_DICT_DISPLAY_SEPARATOR: str = ": "
DEFAULT_CLI_DISPLAY_WIDTH: int = 80
DEFAULT_CLI_FIELD_PADDING: int = 15

# TODO use a class for these strings?
# @dataclass()
# class _tracker(str):
#     """ extended string """
#     pass

# Support functions


def get_var_name(the_var: Any):
    return [
        var_name
        for var_name, var_val in inspect.currentframe().f_back.f_back.f_locals.items()
        if var_val is the_var
    ][0]


def _var_var_name(the_var: Any) -> Tuple[str]:

    print(inspect.currentframe().f_back.f_back.f_locals.items())
    return (
        [
            var_name
            for var_name, var_val in inspect.currentframe().f_back.f_back.f_locals.items()
            if var_val is the_var
        ][0],
        the_var,
    )


def _add_dots(s: str, n: int) -> str:
    """ Truncate string and add ' ...' if needed to fit <s> in <n> spaces

        param :: s:str - string to truncate
        param :: n:int - length of return string
        return :: str - string of length n
        """
    str_len = n - 4
    if len(s) > str_len:
        return s[0 : n - 4] + " ..."
    else:
        return s


def _format_var_value(
    the_string: str,
    padding: int = DEFAULT_CLI_FIELD_PADDING,
    width: int = DEFAULT_CLI_DISPLAY_WIDTH,
    separator: str = DEFAULT_DICT_DISPLAY_SEPARATOR,
) -> str:
    """ Format string for 'var : value' pattern
        param :: s: str - variable to print
        param :: width: int - width of total display - i.e. len(ret_val)
        param :: padding: int - length of name field (0 means calculate)
        param :: separator: str - field separator (default is ': ')
        return :: str - formatted string in the pattern 'var : value'
        """
    padding

    def add(x, y):
        return x + y

    the_string_name = get_var_name(the_string)
    print("get string name: ", the_string_name)
    if padding == 0:
        padding = len(the_string_name)
    if padding < 10:
        padding = 10

    def var_name(the_var):
        return [
            var_name
            for var_name, var_val in inspect.currentframe().f_back.f_locals.items()
            if var_val is the_var
        ][0]

    str_padding = width - padding - len(separator)
    str_format = (
        f"{{:<{padding}.{padding}}}{separator}{{:<{str_padding}.{str_padding}}}"
    )
    result = str_format.format(
        _add_dots(the_string_name, padding), _add_dots(the_string, str_padding)
    )
    # print()
    # print('the_string_name: ', the_string_name)
    # print('... name,padding: ', _add_dots(the_string_name, padding))
    # print()
    # print('... string, str_padding: ', _add_dots(the_string, str_padding))
    print()
    print("str_format: ", str_format)
    print(result)
    return ""


if __name__ == "__main__":
    print()
    print("Debug print values")
    print("******************")
    print()
    # print(_get_var_name(__file__))
    # print('_add_dots(name, 25, 15) : ', _add_dots(name, 25))
    # print('_add_dots(__name__, 25) : ', _add_dots(__name__, 25))
    # print('_add_dots(__file__, 45) : ', _add_dots(__file__, 45))
    # print('_add_dots(__version__, 15) : ', _add_dots(__version__, 15))
    # print('_add_dots(__package__, 25) : ', _add_dots(__package__, 25))
    # print(_var_var_name(__file__))
    print(get_var_name(__file__))
    print("")
    print(_format_var_value(__file__, 5, 80))
    # print(_format_str_dots(__file__, 45))

    # print()
    # print('name        : {:<25.25} '.format(name)[0:21]+' ...')
    # print('__name__    : {:<15.15} '.format(__name__))
    # print('__file__    : {:<45.45} '.format(_add_dots(__file__, 45)))
    # print('__version__ : {:<15.15} '.format(__version__))
    # print('__package__ : {:<25.25} '.format(__package__))
