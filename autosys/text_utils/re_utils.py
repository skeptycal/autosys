#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" # TODO -- @update `AutoSys` package
        copyright (c) 2018 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`


    String CONSTANTS

        ord(NL):  10

        [ord(x) for x in STR_WHITESPACE]=[32, 9, 10, 13, 11, 12]

        STR_HEX='0123456789abcdefABCDEF'`

        STR_ALPHA='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

        STR_ALPHANUMERIC='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

        STR_PUNCTUATION='!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

        STR_PRINTABLE='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'

        [ord(x) for x in STR_PRINTABLE]=[48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 58, 59, 60, 61, 62, 63, 64, 91, 92, 93, 94, 95, 96, 123, 124, 125, 126, 32, 9, 10, 13, 11, 12]
        """

# * --------------------------------- Imports and Constants

# 'Standard Library'
import re

from dataclasses import (
    Field,
    dataclass,
    field,
)

# 'package imports'
from autosys import debug
from random_string import *
from strang import (
    Strang,
    random_string,
)

from typing import (
    Final,
    List,
    Tuple,
)

CASE_LIST: Tuple = ("upper", "lower", "title", "snake", "camel", "pascal")

DEFAULT_RE_FLAGS: Final[int] = re.MULTILINE | re.IGNORECASE

RE_VERSION: re.Pattern = re.compile(
    pattern=r'^__version__\s?=\s?[\'"]([^\'"]*)[\'"]',
    flags=DEFAULT_RE_FLAGS,
)

RE_REPLACE: Final[re.Pattern] = re.compile(pattern=r"[-\s]",
                                           flags=DEFAULT_RE_FLAGS)


class ReUtilsError(Exception):
    "An error occurred while processing regex strings with ReUtils."


__all__ = [
    "CASE_LIST",
    "DEFAULT_RE_FLAGS",
    "NL",
    "NUL",
    "RE_REPLACE",
    "RE_VERSION",
    "ReUtils",
    "ReUtilsError",
    "STR_ALPHA",
    "STR_ALPHANUMERIC",
    "STR_HEX",
    "STR_NAMES",
    "STR_PRINTABLE",
    "STR_PUNCTUATION",
    "STR_WHITESPACE",
    "linesep",
    "random_string",
    "re",
    "re_pip_safe_name",
    "split_it",
    "string",
    "sub_it",
]
if True:  # * --------------------------------- ReUtils Class

    @dataclass
    class ReUtils(Strang):
        """ Wrapper for common Python3 Regex Utilities. """

        string: str = r""

        def __post_init__(self):
            # strip whitespace from ends
            self.string.strip()
            # self.string = self.string.strip()
            # remove duplicate whitespace
            self.dedupe_whitespace()
            self._set_cases()

        def __str__(self):
            return self.string

        def _set_cases(self):
            """ Choose a case by mapping the prefix to the methods.

                e.g.
                ```
                CASE_LIST = ('upper', 'lower', 'title', 'snake', 'camel', 'pascal')

                _cases = {x: f"self.to_{x}_case" for x in CASE_LIST}
                ```
                """

            self._cases = {x: f"self.to_{x}_case" for x in CASE_LIST}

        def re_pip_safe_name(self) -> (str, None, Exception):
            """ Return a name that is converted to pypi safe format.

                Replace ' ' (space) and '-'(hyphen) with _(underscore) using python3 regex
                """
            try:
                return RE.sub_it(string=self.string.lower(),
                                 pattern=RE_REPLACE,
                                 repl="_")
            except Exception as e:
                raise ReUtilsError(e)

        def sub_it(self,
                   pattern: re.Pattern = RE_REPLACE,
                   repl: str = "_") -> (str):
            """ Return a string where items in `pattern` have been replaced with `repl`. """
            try:
                return re.sub(pattern=pattern, repl=repl, string=self.string)
            except Exception as e:
                raise ReUtilsError(e)

        def split_it(self, delimiter: str = "\s") -> (str):
            """ Return a string separated using 'delimiter' using python3 regex. """
            try:
                return re.split(pattern=delimiter, string=self.string)
            except Exception as e:
                raise ReUtilsError(e)

        def clear_all_whitespace(self):
            return self.string.translate(
                {ord(c): None
                 for c in string.whitespace})
            # TODO - which is faster?
            # self.string = "".join(self.string.split())

        def dedupe_whitespace(self):
            """ Return a string with duplicate whitespace replaced with ' '. """
            return re.sub(pattern=r"[\s+]", repl=" ", string=self.string)


def _test():
    test_list1: List[str] = [
        "this is a-test",
        "123_456 789-111",
        "(361) 773-2832",
        ";alskjdfpo82jn sdf83nf ",
    ]

    test_whitespace: List[str] = [
        "  spaces all      over   the    \n places     \t",
        "white\t\n\r\x0b\x0cspace",
        "   fasdf   ",
        "a   b  c     d  e f g hij k  ",
    ]

    test_list: List[str] = []
    test_list.extend(test_whitespace)

    for i in range(20):
        test_list.append(random_string(25))

    re_delimiter = r"[\s-]"
    delimiter = r" -"
    print()
    for item in test_list:
        print("---------------------------------")
        print(item)
        print("---------------------------------")
        s = ReUtils(item)
        print("s:        ", s)
        print("repr:     ", repr(s))
        print("split:    ", s.split_it())
        print("sub:      ", s.sub_it())
        print("upper:    ", s.to_upper_case)
        print("lower:    ", s.to_lower_case)
        print("title:    ", s.to_title_case)
        print("snake:    ", s.to_snake_case)
        print("kebab:    ", s.to_kebab_case)
        print("camel:    ", s.to_camel_case)
        print("pascal:   ", s.to_pascal_case)
        print("clear:    ", s.clear_all_whitespace())


if True == False:  # * --------------------------------- Tests
    _test()
