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
from dataclasses import dataclass, field, Field
from typing import Any, Dict, Final, List, Sequence, Set, Tuple
from os import linesep as NL
import sys
import json

from autosys.text_utils.nowandthen import now

copyright_symbol: str = "©"  # could be (c)
_debug_: bool = True


def my_class(func):
    return str(type(func)).split(".")[-1][:-2]


class PrettyDict(dict):
    def table_dict(
        self,
        table_rows: Dict[str, Any],
        border_char: str = "-",
        divider: bool = True,
    ) -> str:
        """ Returns a table version of a dictionary.

            - table_rows  = dictionary of rows
            - border_char = string used for border

            e.g.
                print(table_dict(my_dict, border_char = "˚`†´", divider = True))
            """
        result: List[str] = []
        longest_string: int = len(max(table_rows, key=len))
        border: str = border_char * (longest_string // len(border_char))
        result.append(border)
        result.append(f"{self._my_class} data for '{self.name}':")
        result.append(border)
        result.extend(table_rows)
        result.append(border)
        return NL.join(result)

    def table_list(
        self, table_rows: List[str], border_char: str = "-",
    ) -> str:
        """ Returns a table version of a list.

            - table_rows  = list of rows
            - border_char = string used for border

            e.g.
                print(table_list(my_rows, border_char = "˚`†´"))
            """
        result: List[str] = []
        longest_string: int = len(max(table_rows, key=len))
        border: str = border_char * (longest_string // len(border_char))
        result.append(border)
        result.append(f"{self._my_class} data for '{self.name}':")
        result.append(border)
        result.extend(table_rows)
        result.append(border)
        return NL.join(result)

    def to_dict(self, include_dunders: bool = False) -> Dict[str, str]:
        """ Returns a formatted dictionary view . """
        if include_dunders:
            return {k: v for k, v in self.items()}
        return {k: v for k, v in self.items() if not k.startswith("_")}

    def thats_all(self, border_char="-") -> str:
        return {k: v for k, v in vars(self).items()}

    def pretty_dict(self, border_char="-") -> str:
        """ Returns a pretty version of dictionary.

            - border_char = string used for border

            e.g.
                print(self.pretty(border_char = "˚`†´"))
        """
        return self.table_list(
            [f"{k:<20.20}: {v}" for k, v in self.to_dict().items()],
            border_char=border_char,
        )

    def to_json(self, sort_keys=True, indent=2):
        return json.dumps(
            version.to_dict(), indent=indent, sort_keys=sort_keys
        )


@dataclass
class MyVersion:
    name: str
    _start_year: int = now.year
    version: str = field(default="0.0.1")
    author: str = field(default="Michael Treanor")
    author_email: str = field(default="skeptycal@gmail.com")
    _license: str = field(default="MIT")
    python_requires: str = field(default=">=3.8")
    _copyright: str = ""

    def __post_init(self):
        if not self.name:
            raise ValueError("Project must have a name.")
        # * >>--------> add other necessary fields here
        for field in __dict__:
            ## add property
            pass

    @property
    def version_info(self) -> Tuple[int, int, int]:
        return self.version.split(".")

    @property
    def license(self) -> str:
        return self._license.upper()

    @property
    def copyright(self) -> str:
        if not self._copyright:
            self._copyright = self._get_copyright_date()
        return self._copyright

    def _get_copyright_date(self) -> str:
        """ Return a correct formatted copyright string. """
        year = now.year
        tmp: str = ""
        try:
            self._start_year = int(self._start_year)
            # include start year if it is in [1900..now]?
            tmp = (
                f"{self._start_year}-"
                if 1900 < self._start_year < year
                else ""
            )
        except:
            self._start_year = year

        return f"Copyright {copyright_symbol} {tmp}{year} {self.author}"

    @property
    def _my_class(self):
        return my_class(self)

    def _export_all(self) -> List[str]:
        """ Returns an '__all__' list.

            Add methods or properties that are not in self.__dict__ that you want to export using the 'extras' parameter.

            e.g.
                [
                    "author",
                    "__author_email__",
                    "__copyright__",
                    "__license__",
                    "__python_requires__",
                    "__title__",
                    "__version__",
                    "__version_info__",
                    "now",
                ] """

        return sorted([x for x in dir(self) if not x.startswith("_")])


version = MyVersion(_start_year=2019, name="AutoSys", version="0.4.4")

__all__ = version._export_all()
if _debug_:
    import json

    _intro = f"{version.name} version {version.version} setup information"
    _hr = "=" * 60
    print(_intro)
    print(version.copyright)
    print()
    print(ASCII_BORDERS.single)
    print([chr(x) for x in ASCII_BORDERS.single])
    for i in range(32, 255):
        print(f"{i}: {chr(i)}")
    print()
    print()
    print(_hr)
    print("__all__ = \n", version._export_all())
    print()
    # print(version.thats_all())
    print(_hr)
    print("dictionary created from 'version.to_dict()'")
    print(_hr)
    # print(version.to_dict())
    print()
    # print(version.pretty_dict())
    print("to_json = ")
    # print(version.to_json())
    print(_hr)
