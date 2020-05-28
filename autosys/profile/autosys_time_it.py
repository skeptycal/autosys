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
if True:  # ?----------------------------------- Imports
    import time
    from typing import Dict, Generator, List
    from functools import lru_cache as lru_cache

    # import timeit
    from time import perf_counter_ns as timer
    from sys import argv, stderr, stdout
    from os import linesep as NL

    _debug_: bool = True


def dbprint(*args, sep=" ", end=NL, file=stderr, flush=False):
    if _debug_:
        print(
            *args, sep=sep, end=end, file=file, flush=flush,
        )


_FIB_FMT: str = "f'{func.__name__:>20.20}({args[0]}) = {result:>5d}   -  {dt:>10d} ns'"

time_list = []


def time_me(func, *args, **kwargs):
    def _timed(func, *args, **kwargs):
        dt = timer()
        result = func(*args, **kwargs)
        dt = timer() - dt

        dbprint("test")
        dbprint(f"{eval(set_fmt())}")
        return (dt, result)

    return _timed


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        dt = (te - ts) * 1000

        time_list.append({method.__name__: f"{dt:4.4}"})
        dbprint(time_list[-1])
        return (result, dt)

    return timed


def _fib(n: int):
    """ Calculates and returns the steps of the Fibonacci Sequence.

        This is the most simple and direct method.

        return:
            int - Fibonacci of <n>
        """
    return _fib(n - 1) + _fib(n - 2) if n > 1 else n


@lru_cache
def _fib_cache(n: int):
    """ Calculates and returns the steps of the Fibonacci Sequence.

        This is the most simple and direct method.

        return:
            int - Fibonacci of <n>
        """
    return _fib(n - 1) + _fib(n - 2) if n > 1 else n


@timeit
def fib(n: int, count: int):
    retval = 0
    for i in range(count):
        result = _fib(n)
        # dbprint(f"'{fib.__name__}' completed {i} trials of fib({n}) = {result}")
        retval += result
    # dbprint(f"'{fib.__name__}' completed {count} trials of fib({n}) sum = {retval}")
    return retval


def repeat(func, *args, count=20, **kwargs):
    retval = 0
    for i in range(count):
        result = func(*args, **kwargs)[1]
        # dbprint(f"'{fib.__name__}' completed {i} trials of fib({n}) = {result}")
        retval += result
    dbprint(f"'{func.__name__}' completed {count} repeats.")
    return retval


# ?----------------------------------- Main Entry Point


def __main__(args=argv[1:]):
    """
    CLI script main entry point.
    """
    x = repeat(fib, 20, 20)


if __name__ == "__main__":  # if script is loaded directly from CLI
    __main__()

# ?----------------------------------- References
