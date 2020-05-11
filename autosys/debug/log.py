#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Part of the `AutoSys` package
        copyright (c) 2019 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """
if True:  # !------------------------ Imports
    import sys
    # import platform
    import logging

    from sys import stdout, stderr, argv
    from enum import unique as _unique, IntEnum as _IntEnum
    # from dis import dis
    # from functools import lru_cache
    # from os import environ as ENV, linesep as NL
    # from pathlib import Path

    from autosys.defaults import *
    from autosys._version import *

    __all__ = [                             # objects exported for 'import *'
        'arg_str',
        'ARGS',
        'br',
        'db_column_ruler',
        'dbprint',
        'Dict',
        'ENV',
        'err',
        'ErrC',
        'Error',
        'hr',
        'IS_64BITS',
        'List',
        'log_error',
        'logex',
        'lru_cache',
        'NL',
        'PLATFORM',
        'read',
        'show_dis',
        'show_version',
        'stderr',
        'stdout',
        'SUPPORTS_COLOR',
        'Terminal',
        'tryit',
        'v_name',
        'verbose',
        'vprint',
    ]
if True:  # !------------------------ CONSTANTS

    if _log_flag_:
        _LOG_PATH: Path = Path().cwd().resolve() / 'log_autosys.log'
        # logging.basicConfig(filename='example.log',
        #                     filemode='w', level=logging.DEBUG)
        logging.basicConfig(filename=_LOG_PATH.as_posix(), level=logging.DEBUG)
        logging.debug(f'Logging is on for {__title__} version {__version__}')
        logging.info(f'  {__copyright__}  -  License: {__license__}')

    # sometimes useful CONSTANTS ...
    # more reliable - https://docs.python.org/3.9/library/platform.html

    class LogSystem():

        def __init__():
            pass
            

if True:  # !------------------------ Logging Utilities
    def info(*args):
        logging.info(*args)

    def log_error(*args):
        """ Error reporting in debug mode.

            current (temporary) behavior: print error messages to <stderr> using dbprint. (if _debug_ flag is True)
            """
        # TODO - fix temporary functionality
        if _log_flag_:
            logging.info(*args)
            dbprint(*args)  # ! temp

    def logex(func):
        """ Decorator to catch and log errors. """
        if _log_flag_:
            try:
                result = func()
            except IOError as e:
                log_error(
                    f'logex caused an error while reporting <{func}>: {e}.')
            else:
                if isinstance(result, Exception):
                    log_error(f'Function <{func}> caught an error: {e}.')
            finally:
                del(e)

    def verbose(v: int, *args, **kwargs):
        """ Print based on '_verbose_' allowed verbosity level.

            v: int - requested verbosity level
            """
        try:  # if _verbose_ constant does not exist, skip this function
            _verbose_ == 0
        except NameError:
            return -1
        if _verbose_ >= v:
            if v < 2:
                kwargs["file"] = "sys.stdout"
                print(*args, **kwargs)
            elif v == 2:
                kwargs["file"] = "sys.stderr"
                print(*args, **kwargs)

if True:  # !------------------------ Script Tests
    def _tests_():
        """ Debug Tests for script. """

        pass


def _main_():  # !------------------------ Script Main
    '''
    CLI script main entry point.
    '''
    if _debug_:
        _tests_()



if __name__ == "__main__":
    _debug_: bool = True                    # True => use Debug features
    _verbose_: int = 0                      # Verbosity level => 0 - 4
    _log_flag_: bool = _debug_ and True     # True => log to file if _debug_
    # argv.append('version')  # ! test
    # argv.append('help')  # ! test
    term = Terminal()
    if 'version' in ARGS:
        show_version()
    else:
        if 'help' in ARGS or 'debug' in ARGS:
            _debug_ = True
        _main_()


""" Error alternates:

    class _Enum_ish(tuple):
        # alternate Enum:
        # ref: https://stackoverflow.com/a/9201329
        __getattr__ = tuple.index
        __setattr__ = None
        __del__ = None


    class _Enum_like(object):
        # alternate Enum
        # ref: https://stackoverflow.com/a/4092436
        values = []

        class __metaclass__(type):
            def __getattr__(self, name):
                return self.values.index(name)

            def name_of(self, i):
                # There's another handy advantage: really fast reverse lookups:
                return self.values[i]

    """
