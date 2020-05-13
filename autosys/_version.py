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

_debug_: bool = False

__version_info__ = (0, 4, 4)
__version__ = ".".join(map(str, __version_info__))
__license__: str = "MIT".upper()
__title__: str = "autosys".title()
__author__: str = "Michael Treanor".title()
__author_email__: str = "skeptycal@gmail.com".lower()


def _get_copyright_date(start_year: int = 0, \
                        _author: str = __author__) -> str:
    from datetime import date

    current_year = date.today().year

    # skip some invalid start_year values
    if not start_year or start_year > current_year or start_year < 1900:
        start_year = current_year

    year_fmt: str = f"{current_year}"
    if start_year != current_year:
        year_fmt = f"{start_year}-{year_fmt}"

    return f'Copyright (c) {year_fmt} {_author}'


__copyright__: str = _get_copyright_date(2018).title()
__python_requires__: str = ">=3.8"

__all__ = [
    '__version_info__', '__version__', '__license__', '__title__',
    '__author__', '__author_email__', '__copyright__', '__python_requires__'
]

if _debug_:
    from datetime import date
    from pprint import pprint
    # day = f'{date:%A}'
    # print(f'--- Today is some {day} in {current_year}, by the way.')
    _intro = f'{__title__.title()} setup and version information:'
    _hr = '=' * len(_intro)
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
