#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" _version.py - version and demographic information

    Part of the `AutoSys` package - utilities for macOS apps
        copyright (c) 2019 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """
from datetime import datetime as _dt 

_year_start: str = '2019'
_year = _dt.now().year
_copyright_year = f'{_year_start}-{_year}'

__version__: str = "0.4.4"
__license__: str = "MIT"
__title__: str = "autosys"
__author__: str = "Michael Treanor"
__author_email__: str = "skeptycal@gmail.com"
__copyright__: str = f"Copyright (c) {_copyright_year} {__author__}"
__python_requires__: str = ">=3.8"

__all__ = [
    '__version__',
    '__license__',
    '__title__',
    '__author__',
    '__author_email__',
    '__copyright__',
    '__python_requires__'
]

if False:
    _intro = f'{__title__.title()} setup and version information:'
    _hr = '=' * len(_intro)
    print(_intro)
    print(_hr)
    
    print(f"{_year_start=}")
    print(f"{_year=}")
    print(f"{_copyright_year=}")
    print()
    print(f"{__version__=}")
    print(f"{__license__=}")
    print(f"{__title__=}")
    print(f"{__author__=}")
    print(f"{__author_email__=}")
    print(f"{__copyright__=}")
    print(f"{__python_requires__=}")
    print(_hr)
