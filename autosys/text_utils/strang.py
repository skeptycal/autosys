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

from random_string import *

from dataclasses import dataclass, Field, field
from os import linesep
from typing import Final, List, Tuple

__all__: List[str] = [
    "CASE_LIST",
    "NL",
    "NUL",
    "STR_ALPHA",
    "STR_ALPHANUMERIC",
    "STR_HEX",
    "STR_NAMES",
    "STR_PRINTABLE",
    "STR_PUNCTUATION",
    "STR_WHITESPACE",
    "StrWrapper",
    "Strang",
    "random_string",
    "string",
]

CASE_LIST: Tuple[str] = ("upper", "lower", "title", "snake", "camel", "pascal")


@dataclass
class StrWrapper:
    """ Generic Wrapper for common Python3 strings.

        :normalize: flag to strip extra whitespace. (default True)

        Contains functions to split, sub, and change case.

        Example:

        ```
        string:         spaces all over the places
        repr:      StrWrapper(string='spaces all over the places')
        split:     ['spaces', 'all', 'over', 'the', 'places']
        sub:       spaces_all_over_the_places
        upper:     SPACES ALL OVER THE PLACES
        lower:     spaces all over the places
        title:     Spaces All Over The Places
        snake:     spaces_all_over_the_places
        kebab:     spaces-all-over-the-places
        camel:     SpacesAllOverThePlaces
        pascal:    spacesAllOverThePlaces
        clear:     spacesallovertheplaces
        ```
        """

    string: str = ""
    normalize: bool = True

    def __post_init__(self):
        if self.normalize:
            # remove leading / trailing whitespace
            self.string = self.string.strip()
            self.dedupe_whitespace()
        self._set_cases()

    def __str__(self):
        return self.string

    def _set_cases(self):
        """ # TODO not yet implemented
            Choose a case by mapping the prefix to the methods.

            e.g.
            ```
            CASE_LIST = ('upper', 'lower', 'title', 'snake', 'camel', 'pascal')

            _cases = {x: f"self.to_{x}_case" for x in CASE_LIST}
            ```
            """

        self._cases = {x: f"self.to_{x}_case" for x in CASE_LIST}

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
        return f"{self.string[0].lower()}{''.join([word.title() for word in self.string.split()])[1:]}"

    @property
    def to_pascal_case(self):
        return "".join([word.title() for word in self.string.split()])

    def split_it(self, delimiter: str = " ") -> (List[str]):
        """ Return a list of strings formed by spliting a string on each 'delimiter' using python3 built-ins. """
        return self.string.split(sep=delimiter)

    def sub_it(self, pattern: str = " -", repl="_") -> (str, None, Exception):
        """ Return a string with elements of `pattern` replaced with `repl` using python3 built-ins. """
        retval: str = ""
        for c in self.string:
            if c in pattern:
                c = repl
            retval += c
        return retval

    def dedupe_whitespace(self):
        """ Remove duplicate whitespace. """
        self.string = " ".join(self.string.split())
        return self.string


@dataclass
class Strang(StrWrapper):
    """ Wrapper for common Python3 Built-in String Utilities. """
    def __post_init__(self):
        super().__post_init__()

    def pip_safe_name(self) -> (str):
        """ Return a name that is converted to pypi safe format.

            Replace ' ' (space) and '-'(hyphen) with _(underscore) using python3 built-ins
            """
        return self.string.lower().replace("- ", "_")

    def clear_all_whitespace(self):
        return self.string.translate({ord(c): None for c in string.whitespace})
        # TODO - which is faster?
        # self.string = "".join(self.string.split())


from autosys.debug.show_all import show_all
