#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Part of the `AutoSys` package - utilities for macOS apps
        copyright (c) 2019 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """

# 'package imports'
from dev.debug import *

# !---------------------------------------------- dev tests


def _tests_():
    x = ""
    print(x)


# !---------------------------------------------- cli features


def _main_():
    """
    CLI script main entry point.
    """
    _debug_: bool = True
    if _debug_:
        _tests_()


if __name__ == "__main__":  # if script is loaded directly from CLI
    _main_()
