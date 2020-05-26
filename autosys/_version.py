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
from typing import Dict, Final, Tuple
from datetime import datetime

_debug_: Final[bool] = True

PROJECT_AUTHOR: Final[str] = "Michael Treanor"
PROJECT_START_YEAR: Final[int] = 2018


class NowAndThen(datetime.today()):
    """ Wrapper for datetime to allow easy access to common functionality. """

    @property
    def year(self):
        """ Return current year. """
        return datetime.today().year

    @property
    def now(self):
        return datetime.today()

    @property
    def week(self):
        """ Return current month number. """
        return datetime.today().month

    @property
    def weekday(self):
        """ Return the current weekday. """
        return datetime.today().strftime("%A")

    def fmt(self, s: str):
        """ Return formatted datetime strings. """
        return datetime.today().strftime(s)

    # def __getattribute__(self, name):

    #     datetime.today().
    #     if hasattr(datetime.today(), name):
    #         print(f"__getattribute__ succeeded with name {name}")
    #         print(f"The response was {datetime.today().__getattribute__(name)}")
    #         return datetime.today().__getattribute__(name)
    #     else:
    #         print(f"  __getattribute__ failed with name {name}")
    #         return datetime.now()
    #         # try:
    #         #     return f"datetime.today().{name}"
    #         # except:
    #         #     return datetime.today().now()
    #     # else:
    #     #     return self.get(name)

    def get_copyright_date(
        self,
        start_year: int = 0,
        _author: str = PROJECT_AUTHOR.title(),
        symbol: str = "(c)",
    ) -> str:
        """ Return a correct formatted copyright string. """
        try:  # if start year is not an integer, fix it
            start_year = int(start_year)
        except:
            start_year = self.year

        if 1900 < start_year < self.year:  # is start year in (1900-now)?
            return f"Copyright {symbol} {start_year}-{self.year} {_author}"
        else:
            start_year = self.year
            return f"Copyright {symbol} {self.year} {_author}"


now = NowAndThen()

__author__: Final[str] = PROJECT_AUTHOR.title()
__version_info__: Final[Tuple[int, int, int]] = (0, 4, 4)
__version__: Final[str] = ".".join(map(str, __version_info__))
__license__: Final[str] = "MIT".upper()
__title__: Final[str] = "autosys".title()
__author_email__: Final[str] = "skeptycal@gmail.com".lower()


__copyright__: Final[str] = now.get_copyright_date(PROJECT_START_YEAR).title()
__python_requires__: Final[str] = ">=3.8"


__all__ = [
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
