# -*- coding: utf-8 -*-
""" Part of the `AutoSys` package
        copyright (c) 2019 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """
__license__ = "MIT"

import os
import sys

# !---------------------------------------------- String Utilities

NL: str = os.linesep


def arg_str(*args, sep=' ') -> str:
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
                dbprint(f'An argument could not be converted to a string for display - {arg}')
            except:
                pass  # skip debug output if not available
            pass  # skip args that cannot be converted to strings
    return sep.join(_)


def br(n: int = 1) -> int:
    """ Yes, this is a CLI version of a <br /> tag ...

        n : int - number of line breaks to print

        return int 0 for success else 1
        """
    try:
        print(NL*n, end='', sep='')
        return 0
    except:
        return 1


def brerr(n: int = 1) -> int:
    """ Yes, this is a CLI version of a <br /> tag ... sent to STDERR.

        n : int - number of line breaks to print

        return int 0 for success else 1
        """
    try:
        print('\n'*n, end='', sep='', file=sys.stderr)
        return 0
    except:
        return 1


def hr(s: str = '-', n: int = 79) -> str:
    """ Print a string duplicated <n> times.

        This can act as a page break. Yes, this is a CLI version of an <hr /> tag

        s : str  - string to repeat (default '-')
        n : int  - number of times to repeat (default 79)
        """
    print(s*n)
