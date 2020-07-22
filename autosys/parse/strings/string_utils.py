# -*- coding: utf-8 -*-
""" Part of the `AutoSys` package
        copyright (c) 2019 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """
__license__ = "MIT"

# 'Standard Library'
import os
import re
import sys

from os import linesep as NL

# !---------------------------------------------- String Utilities


def split_it(s: str, delimiter: str = "\s"):
    return re.split(pattern=s, string=delimiter)


def arg_str(*args, sep=" ") -> (str):
    """ Return one string created from *args sequence.

        sep - string used in between joined elements.

        each element is converted to a string where possible, otherwise
        it is ignored and silently logged as an error
        """
    from typing import Any, List

    _: List[Any] = []
    for arg in args:
        try:  # convert args to strings
            _.append(str(arg))
        except:
            try:
                log.error(
                    f"An argument could not be converted to a string for display - {arg}"
                )
            except:
                pass  # skip debug output if not available
    return sep.join(_)


def brerr(n: int = 1) -> (int):
    """ Yes, this is a CLI version of a <br /> tag ... sent to STDERR.

        n : int - number of line breaks to print

        return int 0 for success else 1
        """
    try:
        print("\n" * n, end="", sep="", file=sys.stderr)
        return 0
    except:
        return 1
