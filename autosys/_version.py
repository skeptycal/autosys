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
from dataclasses import dataclass
from typing import Dict, Final, List, Sequence, Tuple
import sys

from autosys.text_utils.nowandthen import now

_debug_: bool = True
__version__ = "0.4.4"
__title__ = "AutoSys"


@dataclass
class MyVersion:
    start_year: int
    __title__: str
    __version__: str = __version__
    __author__: str = "Michael Treanor"
    __author_email__: str = "skeptycal@gmail.com"
    __license__: str = "MIT"
    __python_requires__: str = ">=3.8"
    __copyright__: str = ""

    def __post_init(self):
        __copyright__ = now.get_copyright_date(
            start_year=self.start_year, _author=self.__author__
        ).title()
        # * >>--------> add other necessary fields here
        for field in __dict__:
            ## add property
            pass

    @property
    def title(self) -> str:
        self.__title__

    @property
    def author(self) -> str:
        self.__author__.title()

    @property
    def author_email(self) -> str:
        self.__author_email__.lower()

    @property
    def license(self) -> str:
        self.__license__.upper()

    @property
    def python_requires(self) -> str:
        self.__python_requires__

    @property
    def __version_info__(self, version: str) -> Tuple[int, int, int]:
        return self.__version__.split(".")

    @property
    def copyright(self) -> str:
        if not self.__copyright__:
            self.__copyright__ = now.get_copyright_date(
                start_year=self.start_year, _author=self.__author__
            )
        return self.__copyright__

    def __all__(self, extras=["now"]) -> List[str]:
        """ Returns an '__all__' list.

            Add methods or properties that are not in self.__dict__ that you want to export using the 'extras' parameter.

            e.g.
                [
                    "__author__",
                    "__author_email__",
                    "__copyright__",
                    "__license__",
                    "__python_requires__",
                    "__title__",
                    "__version__",
                    "__version_info__",
                    "now",
                ] """
        tmp: List[str] = [x for x in self.__dict__]
        if extras:  # only Sequences will be added
            if isinstance(extras, str):  # append strings ...
                tmp.append(extras)
            elif isinstance(extras, Sequence):  # extend others
                tmp.extend((extras))
        return tmp

    def to_dict(self):
        """ Returns a dictionary of properties.

        e.g.
            ===================================
            to_dict =
            {'start_year': 2018,
            '__title__': 'AutoSys',
            '__version__': '0.4.4',
            '__author__': 'Michael Treanor',
            '__author_email__': 'skeptycal@gmail.com',
            '__license__': 'MIT',
            '__python_requires__': '>=3.8',
            '__copyright__': 'Copyright (c) 2018-2020 Michael Treanor'}
            ===================================

        """
        return {arg: self.__getattribute__(f"{arg}") for arg in self.__dict__}


version = MyVersion(start_year=2018, __title__=__title__)

if _debug_:
    from datetime import datetime
    from pprint import pprint

    _intro = f"{version.title } setup and version information:"
    _hr = "=" * len(_intro)
    print(_intro)

    print()
    print(version.copyright)
    print()
    print(_hr)
    for arg in version.__dict__:
        x = f"version.{arg}"
        print(f"  version.{arg:<25.25} = {eval(f'version.{arg}')}")

    print(_hr)
    print("__all__ = ")
    print(version.__all__())
    print(_hr)
    print("to_dict = ")
    print(version.to_dict())
    print(_hr)
    #    _meta_data = {k: eval(k) for k in __all__}
    #    pprint(_meta_data)
    # for f in _fields:
    #     print(f"{f} - {eval(f)}")
    #     print('-' * 50)
    print()
    print(_hr)
