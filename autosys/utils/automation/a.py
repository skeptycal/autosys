#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Part of the `AutoSys` package - utilities for macOS apps
        copyright (c) 2019 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """

# TODO - this is just a rough idea ... not yet implemented ... not functional

from profiling.timeit import *
from io import TextIOWrapper
import sys
from typing import List
from cli.anansi import *
from dev.debug import logit, log

LOG_FILE: TextIOWrapper = sys.stdout
__all__: List[str] = []
ansi = Ansi


def a(func):
    def _all(*args, **kwargs):
        result = func(*args, **kwargs)
        name = func.__name__
        print(f'a({name}) is {result}')
        if name not in __all__:
            __all__.append(name)
        return result
    return _all


@timeit
@try_it
@a
def test_all_decorator(*args, **kwargs):
    print(ansi.BBRIGHTBLUE, ' ** test all the decorators')
    print(1/0)


test_all_decorator('try this stuff')
print(f"__all__ = {__all__}")
