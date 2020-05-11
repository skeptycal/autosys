#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" AutoSys Common Resources

    Common imports, CONSTANTS, and utilities for the `AutoSys` package. These are resources that are used by many modules or functions.

    ---------------------------------------------------------------------------
    Resource: imports - best practices
    - https://stackoverflow.com/a/37126790

        ```
        import package.a           # (1) Absolute import
        # (2) Absolute import bound to different name
        import package.a as a_mod
        from package import a      # (3) Alternate absolute import
        # (4) Implicit relative import (deprecated, python 2 only)
        import a
        from . import a            # (5) Explicit relative import
        ```

        Part of the `AutoSys` package - utilities for macOS apps
        copyright (c) 2019 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

        `AutoSys` is licensed under the `MIT License
            `<https://opensource.org/licenses/MIT>`
    """
from ._version import *
from .defaults import *
# from autosys.defaults import _debug_, _verbose_, _log_flag_

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
