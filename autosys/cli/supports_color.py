#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" supports_color - terminal color detection and setup

    Part of the `AutoSys` package - utilities for macOS apps
        copyright (c) 2019 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """

# 'Standard Library'
from os import environ as ENV
from platform import platform as PLATFORM
from sys import path as PYTHONPATH, stderr, stdout

from typing import Dict, List


def _SUPPORTS_COLOR() -> (bool):
    # generic script level stderr output characteristics
    _IS_A_TTY: bool = stdout.isatty() and hasattr(stdout, "isatty")
    _IS_PPC: bool = PLATFORM() == "Pocket PC"
    _IS_WIN32: bool = PLATFORM() == "win32"
    IS_WIN: bool = "win" in PLATFORM().lower()
    _IS_ANSICON: bool = "ANSICON" in ENV
    _IS_WIN_COLOR: bool = _IS_WIN32 and _IS_ANSICON
    _IS_EDGE_CASE: bool = _IS_WIN_COLOR and not _IS_PPC
    retval = _IS_A_TTY or _IS_EDGE_CASE
    return retval


SUPPORTS_COLOR: bool = _SUPPORTS_COLOR()
print(SUPPORTS_COLOR)
