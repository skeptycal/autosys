#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Common imports, CONSTANTS, and utilities for the `AutoSys` package

    Part of the `AutoSys` package - utilities for macOS apps
        copyright (c) 2019 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """

if True:  # !------------------------ config
    import re

    from functools import lru_cache

    from autosys._version import __version__ as VERSION
    from autosys.debug import db_column_ruler, dbprint
    from autosys.defaults import *

    from autosys.cli import anansi, ascii_codes, colors
    _debug_: bool = True  # True => use Debug features

    # generic script level stderr output characteristics
    _IS_A_TTY: bool = stderr.isatty() and hasattr(stderr, "isatty")
    _IS_PPC: bool = PLATFORM == "Pocket PC"
    _IS_WIN32: bool = PLATFORM == "win32"
    IS_WIN: bool = "win" in PLATFORM.lower()
    _IS_ANSICON: bool = "ANSICON" in ENV
    _IS_WIN_COLOR: bool = _IS_WIN32 and _IS_ANSICON
    _IS_EDGE_CASE: bool = _IS_WIN_COLOR and not _IS_PPC
    SUPPORTS_COLOR = _IS_A_TTY or _IS_EDGE_CASE

    _DB_PREFIX: str = _DEBUG_COLOR * SUPPORTS_COLOR
    _DB_SUFFIX: str = _RESET * SUPPORTS_COLOR