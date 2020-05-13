#!/usr/bin/env python3
# -*- coding: utf-8 -*-
    # shellcheck source=/dev/null
    # shellcheck disable=2230,2086
f""" Part of the `AutoSys` package - utilities for macOS apps

        copyright (c) 2019 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`

    Usage: {__file__} [-h|-v] FILE

    """
if True: # ?----------------------------------- Imports
    import time
    from typing import Dict, Generator
    from functools import lru_cache as lru_cache
    # import timeit
    from time import perf_counter_ns as timer
    from autosys import dbprint, SUPPORTS_COLOR
    from docopt import docopt
    from sys import argv

# ?----------------------------------- Notes
# TODO --- make searchble dict of 3d product models

# ?----------------------------------- Constants


# ?----------------------------------- Private Utilities


# ?----------------------------------- Public Utilities
def time_me(function):
    def wrap(*arg):
        start = time.time()
        r = function(*arg)
        end = time.time()
        print("%s (%0.3f ms)" % (function.func_name, (end-start)*1000))
        return r
    return wrap

# ?----------------------------------- Classes
class Benchmark():
    _DEFAULT_TIME_UNITS = 'ns'
    _DEFAULT_FMT = "f'{fname:>20.20}({args[0]}) = {result:>5d}   -  {dt:>10d} ns'"
    TIME_UNITS: Dict[str, int] = {
        'ns': 9,
        'us': 6,
        'ms': 3,
        's': 0
    }

    def __init__(self, fmt: str = _DEFAULT_FMT, units: str = _DEFAULT_TIME_UNITS, precision: int = 5):
        super().__init__()
        self._fmt: str = fmt
        if units in self.TIME_UNITS:
            self._units = units
            dbprint(self._units)
            self.multiple: int = self.TIME_UNITS[self._units]
            dbprint(self.multiple)
        self._precision: int = precision
        locals()

    def set_fmt(self, f: str = _DEFAULT_FMT) -> str:
        """ Set the output format string for the <time_it> decorator.

            Keyword Arguments:
                f {str} -- time_it output string (default: {_DEFAULT_FMT})

            Returns:
                str -- formatted string
            """
        try:
            return str(f) if f else ''
        except:
            return ''

    def _timed(self, func, *args, **kwargs):
        dt = timer()
        result = func(*args, **kwargs)
        dt = timer() - dt
        return (dt, result)

    def time_it(self, func) -> int:
        """ A decorator to provide performance timing measurement of <func>.

            Arguments:
            - func {function or method} -- code block to be timed

            Returns:
            - int -- nanoseconds elapsed during <func> execution

            #### Example:

            ```py
                @time_it
                def fib(n):
                    return fib(n-1) + fib(n-2) if n > 1 else n

                # pre-formatted f-string template for time_it output
                _FIB_FMT: str = "f'{fname:>20.20}({args[0]}) = {result:>5d}   -  {dt:>10d} ns'"


                def _fib(n: int) -> int:
                    return _fib(n-1) + _fib(n-2) if n > 1 else n


                @time_it
                def fib(n: int) -> int:
                    ''' Wrapper to return Fibonacci Sequence of <n>. '''
                    return _fib(n)


                for i in range(10):
                    x = fib(i)


            ```

            """
        def _timed(*args, **kwargs):
            fname = func.__name__
            dt = timer()
            result = func(*args, **kwargs)
            dt = timer() - dt

            print(f"{eval(set_fmt())}")

            return result
        return _timed

    @lru_cache
    def time_it_cached(self, func):
        """ An alternate version of <time_it> that uses caching. """
        return _timed(func)

    def time_it(self, func):
        pass


# pre-formatted f-string template for time_it output
_FIB_FMT: str = "f'{fname:>20.20}({args[0]}) = {result:>5d}   -  {dt:>10d} ns'"


def _fib(n: int) -> int:
    ''' Calculates and returns the steps of the Fibonacci Sequence.

        This is the most simple and direct method.

        return:
            int - Fibonacci of <n>
        '''
    return _fib(n-1) + _fib(n-2) if n > 1 else n

# ?----------------------------------- Script Tests

def fib(n: int) -> int:
    ''' Wrapper to return Fibonacci Sequence of <n>. '''
    return _fib(n)


def __tests__(args) -> int:
    """ Run Debug Tests for script if _debug_ = True. """
    _test_file(args)
    return 0
# ?----------------------------------- Main Entry Point


def __main__(args: List[str] = []) -> int:
    ''' CLI script main entry point. '''
    # set_script_in_sys_path()

    #! script testing
    if _debug_:
        __tests__(args)
    __run__(args)
    return 0

def __main__():
    '''
    CLI script main entry point.
    '''
    _debug_: bool = True
    b = Benchmark(units='ns')
    for i in range(10):
        x = fib(i)


if __name__ == "__main__":  # if script is loaded directly from CLI

    args = sys.argv[1:]
    __main__(args)

# ?----------------------------------- References
