#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" AutoSys Defaults (defaults.py) - common resources for all `autosys` modules

    Part of the `AutoSys` package - utilities for macOS apps
    copyright (c) 2019 Michael Treanor
    https://www.github.com/skeptycal/autosys
    https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """

# * ------------------------------------------- Common Imports

import logging
from os import environ as ENV, linesep as NL, sep as PATHSEP
from pathlib import Path
from platform import (
    platform, python_implementation as WHICH_PY, system as WHICH_OS,)
from pprint import pformat
from sys import (
    argv, maxsize, path as PYTHON_PATH, stderr, stdout, version_info,)
from typing import (
    Any, Dict, Final, Iterable, List, NamedTuple, Sequence, Tuple,)

from autosys._version import *

# * ------------------------------------------- Common Constants

DEFAULT_LOG_FILE_NAME: str = "log_autosys_private.log"

# sys.maxsize is more reliable than platform
# Ref: https://docs.python.org/3.9/library/platform.html
IS_64BITS: bool = maxsize > 2 ** 32

# is python 3 or above
PY3 = version_info.major >= 3
PLATFORM = platform()
""" ---------------------------------------------------------------------------
    *Goals for dependency imports:

        1. Only import what is needed
            - avoid importing everything all the time
            - use what is needed for the code

        2. Clearly show dependencies at the top of the module
            - standard library imports can be centralized in __init__.py

        3. Defer import until later (specific cases)
            - this should be avoided since it hides `import` statements all
                over the code base
            - make a comment in the `imports` section to clarify

        4. Use absolute imports
            - they can become very long
            - code folding in VSCode with 'if True:' blocks is my hacky fix

    *Reference: imports - best practices
        - https://stackoverflow.com/a/37126790
        "1. Errors importing modules with circular imports"

        ```
        import package.a           # (1) Absolute import
        import package.a as a_mod  # (2) Absolute import bound to different name
        from package import a      # (3) Alternate absolute import
        import a                   # (4) Implicit relative import (deprecated, python 2 only)
        from . import a            # (5) Explicit relative import
        ```

        Unfortunately, only the 1st and 4th options actually work when you have circular dependencies (the rest all raise ImportError or AttributeError). In general, you shouldn't be using the 4th syntax, since it only works in python2 and runs the risk of clashing with other 3rd party modules.

        *So really, only the first syntax is guaranteed to work.*

        The ImportError and AttributeError issues only occur in python 2. In python 3 the import machinery has been rewritten and all of these import statements (with the exception of 4) will work, even with circular dependencies. While the solutions in this section may help refactoring python 3 code, they are mainly intended for people using python 2.

    ---------------------------------------------------------------------------
    """
""" <aside>            NewLine, A Bit of Lore

    Newline is a control character or sequence of control characters in a
    character encoding specification (e.g. ASCII or EBCDIC) that is used to
    signify the end of a line of text and the start of a new one.

    In the mid-1800s, long before the advent of teletype machines, Morse code
    operators invented and used Morse code prosigns to encode white space
    text formatting in formal written text messages. Two 'A' characters sent
    without the normal spacing is used to indicate a new line of text.

    --------------------------------------------------------------------------

    - In computing and telecommunication, a control character or non-printing
        character (NPC) is a code point (a number) in a character set, that
        does not represent a written symbol.

    - During the 1960s, ISO and ASA (who later became ANSI), simultaneously
        developed ASCII for modern teleprinters. The sequence they agreed on
        for newline was CR+LF. This sequence carried forward to the first
        computers that had to share printers with other older devices.

    - The separation of newline into two functions concealed the fact that the
        print head could not return from the far right to the beginning of the
        next line in time to print the next character. Any character printed
        after a CR would often print as a smudge in the middle of the page
        while the print head was still moving the carriage back to the first
        position.

    - Many early video displays also required multiple character times to scroll
        the display. MS-DOS adopted CP/M's CR+LF standard to be compatible. When
        the widespread adoption of the personal computer, the tradition became
        imprinted in newer versions of DOS and Windows.

    - During the same period, Multics (1964) used only the LF character because
        CR was useful for bold and strikethrough effects. This convention was
        adopted by ISO in 1967 and later by UNIX. All UNIX based operating
        systems carried the LF flag forward, with one exception being Apple.

    - The Apple II computer, as well as Commodore, TRS-80, classic Mac OS used CR
        alone. This led to even greater confusion as files encoded on Unix, Apple,
        and Dos based operating systems were all using ASCII encoding and yet were
        frustratingly mutually incompatible.

    - Apple has since joined the Multics crowd and ends lines with LF (0A) instead
        of the old CR (0D). Microsoft has continued to use the 2 character set for
        encoding line endings, but software drivers have eliminated most of the
        prior confusion.

    </aside>
    """
