#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# ============================================================================
# Copyright (c) 2019 Michael Treanor
# MIT <https://opensource.org/licenses/MIT>
# Michael Treanor  <skeptycal@gmail.com>
# https://www.github.com/skeptycal
# Intended for Python 3.0+ , ymmv on 2.7
# ============================================================================


from __future__ import absolute_import, print_function, unicode_literals

import codecs
import csv
import datetime
import inspect
import json
import locale
import logging
import ntpath
import os
import posixpath
import pprint
import re
import shutil
import string
import sys
import time
from collections import OrderedDict, defaultdict
from typing import Any, Dict, List


# import text_colors

sys.path.insert(0, os.path.abspath('.'))

_SCRIPT_START_TIME: float = time.time()
SET_DEBUG: bool = True            # set to True for verbose testing

# TODO
#   - automate creation of TOC
#   - use       declare -F
"""
Return True if a string's  name is safe to use as an attribute name.
"""
is_valid_name = re.compile(r'^[A-Za-z_][A-Za-z0-9_]*$').match

# * ######################## path variables
# script_name="${BASH_SOURCE##*/}"
# script_path="${BASH_SOURCE%/*}"
# src_path="${script_path}/src"
# bak_path="${script_path}/bak"
# bin_path="${HOME}/bin/utilities/pc_bak"
# dotfiles_path="${HOME}/.dotfiles"
# here="$PWD"


class general_function_handler(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, obj, type=None):
        return self.__class__(self.func.__get__(obj, type))

    def __call__(self, *args, **kwargs):
        try:
            retval = self.func(*args, **kwargs)
        except Exception as e:
            logging.warning('Exception in %s' % self.func)
            template = "An exception of type {0} occured. Arguments:\n{1!r}"
            message = template.format(type(e).__name__, e.args)
            logging.exception(message)
            sys.exit(1)  # exit on all exceptions for now
        return retval

# * ######################## ANSI constants for common colors


class textcolors:
    class bash_colors:
        MAIN = '\001\033[38;5;229m'
        WARN = '\001\033[38;5;203m'
        COOL = '\001\033[38;5;38m'
        BLUE = '\001\033[38;5;38m'
        GO = '\001\033[38;5;28m'
        CHERRY = '\001\033[38;5;124m'
        CANARY = '\001\033[38;5;226m'
        ATTN = '\001\033[38;5;178m'
        PURPLE = '\001\033[38;5;93m'
        RAIN = '\001\033[38;5;93m'
        WHITE = '\001\033[37m'
        RESTORE = '\001\033[0m\002'
        RESET_FG = '\001\033[0m'

    def color(self, parameter_list):

        pass

    def me(self, *args, **kwargs):
        print(MAIN, *args, RESET_FG, **kwargs)

# * ######################## constants


DEFAULT_ENCODING: str = 'UTF-8'
DEFAULT_CSV_DELIMITER: str = ','


def now() -> str:
    """
    Return current date and time as formatted string.
    """
    return str(datetime.datetime.now())[0:19]


def lineno() -> int:
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno


def _debug_function_header():
    if SET_DEBUG:
        try:
            caller = inspect.getframeinfo(inspect.currentframe().f_back)
            print(MAIN, "Calling Function: ",
                  CANARY, caller.function,
                  MAIN, "Line: ",
                  CANARY, caller.lineno)
            return 0
        except AttributeError:
            return 1


def db_echo(*args, **kwargs):
    # if log ... log to file
    _debug_function_header()
    if SET_DEBUG:
        print(WARN, "debug info ", COOL, str(now())[
              0:19], RESET_FG, ' - ', *args, **kwargs)


def _test_it(method):  # @decorator - assertion tests
    def _assert(*args, **kw):
        result = method(*args, **kw)
        # print("{} ({}, {}) {:2.2f} sec".format(method.__name__, args, kw, te-ts))
        return result

    return _assert
    pass


def timeit_print(method):  # @decorator - print timer report for a function
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        # print("{} ({}, {}) {:2.2f} sec".format(method.__name__, args, kw, te-ts))
        print("Timing Test: {}{} {}{} {:2.2f} sec".format(
            BLUE, method.__name__, RESET_FG, args, te-ts))
        return result

    return timed


@_test_it
def _run_tests() -> int:
    @timeit_print
    def _math_test(n):
        return sum(i*2 for i in range(n))

    print()
    print(MAIN, "Testing ...")
    print('*'*60, RESET_FG)
    try:
        assert(lineno() == inspect.currentframe().f_lineno)
        me("This is line number ", lineno())
        # print(_math_test(333333))
        assert(_math_test(333333) == 111110555556)
        assert(_debug_function_header() == 0)
        db_echo("test db_echo")
    except AssertionError:
        db_echo("Assertion Error")


if SET_DEBUG:
    _run_tests()
