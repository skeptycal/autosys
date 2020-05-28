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

from typing import Dict, Final, List, Tuple
from autosys.text_utils.nowandthen import *

_debug_: bool = True

PROJECT_AUTHOR: Final[str] = "Michael Treanor"
PROJECT_START_YEAR: Final[int] = 2018


__author__: Final[str] = PROJECT_AUTHOR.title()
__version_info__: Final[Tuple[int, int, int]] = (0, 4, 4)
__version__: Final[str] = ".".join(map(str, __version_info__))
__license__: Final[str] = "MIT".upper()
__title__: Final[str] = "AutoSys".title()
__author_email__: Final[str] = "skeptycal@gmail.com".lower()
__copyright__: Final[str] = now.get_copyright_date(PROJECT_START_YEAR).title()
__python_requires__: Final[str] = ">=3.8"


__all__: List[str] = [
    "__version_info__",
    "__version__",
    "__license__",
    "__title__",
    "__author__",
    "__author_email__",
    "__copyright__",
    "__python_requires__",
    "now",
]

_meta_data: Final[Dict] = {k: eval(k) for k in __all__}

if _debug_:
    from datetime import datetime
    from pprint import pprint

    print(f"")
    print(f"--- Today is some {now.weekday} in {now.year}, by the way.")

    _intro = f"{__title__.title()} setup and version information:"
    _hr = "=" * len(_intro)
    print(_intro)
    print(_hr)
    _meta_data = {k: eval(k) for k in __all__}
    pprint(_meta_data)
    # for f in _fields:
    #     print(f"{f} - {eval(f)}")
    #     print('-' * 50)
    print()
    print(_hr)
    print(f"{__version_info__=}")
    print(f"{__version__=}")
    print(f"{__license__=}")
    print(f"{__title__=}")
    print(f"{__author__=}")
    print(f"{__author_email__=}")
    print(f"{__copyright__=}")
    print(f"{__python_requires__=}")
    print(_hr)
