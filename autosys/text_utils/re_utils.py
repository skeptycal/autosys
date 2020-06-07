#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" `AutoSys` package
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

from random_string import *

import re
from dataclasses import dataclass, Field, field
from typing import Final, List, Tuple

CASE_LIST: Tuple = ("upper", "lower", "title", "snake", "camel", "pascal")

DEFAULT_RE_FLAGS: Final[int] = re.MULTILINE | re.IGNORECASE


if True:  # * --------------------------------- ReUtils Class

    @dataclass
    class ReUtils:
        """ Wrapper for common Python3 Regex Utilities. """

        import re

        DEFAULT_RE_FLAGS: Final[int] = re.MULTILINE | re.IGNORECASE
        RE_REPLACE: Final[re.Pattern] = re.compile(
            pattern=r"[-\s]", flags=DEFAULT_RE_FLAGS
        )

        string = r""

        def sub_it(
            self, pattern: re.Pattern = RE_REPLACE, repl: str = "_"
        ) -> (str, None, Exception):
            """ Return a string where items in `pattern` have been replaced with `repl`. """
            return re.sub(pattern=pattern, repl=repl, string=self.string)

        def re_pip_safe_name(self) -> (str, None, Exception):
            """ Return a name that is converted to pypi safe format.

                Replace ' ' (space) and '-'(hyphen) with _(underscore) using python3 regex
                """
            return RE.sub_it(string=self.string, pattern=RE_REPLACE, repl="_")

        def split_it(self, delimiter: str = "\s") -> (str, None, Exception):
            """ Return a string separated using 'delimiter' using python3 regex. """
            return re.split(pattern=delimiter, string=self.string)

        def dedupe_whitespace(self):
            """ Return a string with duplicate whitespace replaced with ' '. """
            return re.sub(pattern=r"\s+", repl=" ", string=self.string)


# * --------------------------------- Strang Class


@dataclass
class Strang:
    """ Wrapper for common Python3 Built-in String Utilities. """

    if True:  # * --------------------------------- Config
        string: str = ""

        def __post_init__(self):
            # strip whitespace from ends
            self.string = self.string.strip()
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

    if True:  # * --------------------------------- Cases

        @property
        def to_upper_case(self):
            return self.string.upper()

        @property
        def to_lower_case(self):
            return self.string.lower()

        @property
        def to_title_case(self):
            return self.string.title()

        @property
        def to_snake_case(self):
            return self.sub_it().lower()

        @property
        def to_kebab_case(self):
            return self.sub_it(pattern=" _", repl="-").lower()

        @property
        def to_camel_case(self):
            return "".join([word.title() for word in self.string.split()])

        @property
        def to_pascal_case(self):
            return f"{self.string[0].lower()}{''.join([word.title() for word in self.string.split()])[1:]}"

    if True:  # * --------------------------------- Utilities

        def pip_safe_name(self) -> (str):
            """ Return a name that is converted to pypi safe format.

                Replace ' ' (space) and '-'(hyphen) with _(underscore) using python3 built-ins
                """
            return self.string.lower().replace("- ", "_")

        def sub_it(self, pattern: str = " -", repl="_") -> (str, None, Exception):
            """ Return a string with elements of `pattern` replaced with `repl` using python3 built-ins. """
            retval: str = ""
            for c in self.string:
                if c in pattern:
                    c = repl
                retval += c
            return retval

        def split_it(self, delimiter: str = " ") -> (List[str]):
            """ Return a list of strings formed by spliting a string on each 'delimiter' using python3 built-ins. """
            return self.string.split(sep=delimiter)

        def clear_all_whitespace(self):
            return self.string.translate({ord(c): None for c in string.whitespace})
            # TODO - which is faster?
            # self.string = "".join(self.string.split())

        def dedupe_whitespace(self):
            self.string = " ".join(self.string.split())


if True:  # * --------------------------------- Tests

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

    s: Strang = Strang()
    re_delimiter = r"[\s-]"
    delimiter = r" -"
    print()
    for item in test_list:
        print("---------------------------------")
        print(item)
        print("---------------------------------")
        s = Strang(item)
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
