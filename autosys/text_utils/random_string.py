#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" `AutoSys` package
        copyright (c) 2018 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """

import string
from os import linesep
from random import choice

NUL: str = chr(0)
NL: str = linesep

STR_ALPHA: str = string.ascii_letters
STR_ALPHANUMERIC: str = string.ascii_letters + string.digits
STR_HEX: str = string.hexdigits
STR_NAMES: str = string.ascii_letters + " _-"
STR_WHITESPACE: str = string.whitespace
STR_PRINTABLE: str = string.printable
STR_PUNCTUATION: str = string.punctuation


def random_string(string_length=8, pool: str = STR_NAMES):
    """ Returns a string of length 'string_length' made up of characters
        from the string 'pool' """
    return "".join(choice(pool) for _ in range(string_length))
