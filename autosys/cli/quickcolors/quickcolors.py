#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Quick Colors

    quick, simple tags to use in place of Colorama variables as well as
    a simple regex parser to do the tag replacement


    Colorama Color Constants are:
    - Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
    - Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
    - Style: DIM, NORMAL, BRIGHT, RESET_ALL

    More info about [Colorama][4]
    ---
    Part of the [AutoSys][1] package

    Copyright (c) 2018 [Michael Treanor][2]

    AutoSys is licensed under the [MIT License][3]

    [1]: https://www.github.com/skeptycal/autosys
    [2]: https://www.twitter.com/skeptycal
    [3]: https://opensource.org/licenses/MIT
    [4]: https://pypi.org/project/colorama/
    """


# import os
import re

from functools import lru_cache
# from dataclasses import Field, dataclass, field
from os import linesep as NL
# from pathlib import Path
# from shutil import rmtree as _rmtree
from sys import stdout

import setup

from typing import Dict, Final, List

# from colorama import Back, Fore, Style


quick_colors: Final[Dict[str, str]] = {
    '<K>': '\x1b[30m',  # K is black
    '<B>': '\x1b[34m',  # Blue
    '<C>': '\x1b[36m',  # Cyan
    '<G>': '\x1b[32m',  # Green
    '<M>': '\x1b[35m',  # Magenta
    '<R>': '\x1b[31m',  # Red
    '<W>': '\x1b[37m',  # White
    '<Y>': '\x1b[33m',  # Yellow
    '<LK>': '\x1b[90m',  # light colors
    '<LB>': '\x1b[94m',
    '<LC>': '\x1b[96m',
    '<LG>': '\x1b[92m',
    '<LM>': '\x1b[95m',
    '<LR>': '\x1b[91m',
    '<LW>': '\x1b[97m',
    '<LY>': '\x1b[93m',
    '<X>': '\x1b[39m',  # X is for reset
}

# tag format is '<Xx>' - either one or two characters
RE_QUICK_COLOR_TAG: Final[re.Pattern] = re.compile(r'<\w{1,2}>')

# reset constant for trailing reset
RESET_ALL: Final[str] = '\x1b[0m'


@lru_cache
def re_quick_color(s: str) -> (re.Match, None):
    ''' return the next quick color tag match
        (converted to uppercase) or None '''
    try:
        return re.search(RE_QUICK_COLOR_TAG, s)[0].upper()
    except TypeError:
        return None


@lru_cache
def quick_color(s: str) -> (str):
    ''' replace 'quick codes' with ansi escaped sequences from
        Colorama foreground codes

        example:
        ```
        # instead of typing:
        print(f"{Fore.GREEN}{Back.WHITE}{Styles.BOLD}OK{Fore.RESET}{Back.RESET}")

        # you can type:
        qprint("<g>OK")
        ```

        The 'quick codes' are inline literal strings that are similar to
        html tags and are used as placeholders for regex replacement with
        Colorama ansi codes.

        They may be upper or lower case. The trailing 'reset' code is added
        automatically to eliminate color bleeding to upcoming lines.

            # standard colors
            <K>  or  <k>    # K is black
            <B>  or  <b>    # Blue
            <C>  or  <c>    # Cyan
            <G>  or  <g>    # Green
            <M>  or  <m>    # Magenta
            <R>  or  <r>    # Red
            <W>  or  <w>    # White
            <Y>  or  <y>    # Yellow

            # light colors
            <LK> or <lk>    # light black
            <LB> or <lb>    # light Blue
            <LC> or <lc>    # light Cyan
            <LG> or <lg>    # light Green
            <LM> or <lm>    # light Magenta
            <LR> or <lr>    # light Red
            <LW> or <lw>    # light White
            <LY> or <ly>    # light Yellow

            <x> or <X>    # X is for reset
        '''

    while (tag := re_quick_color(s)):
        s = re.sub(pattern=tag, repl=quick_colors[tag], string=s)
    return s


@lru_cache
def qprint(*args, reset_color=True, sep=' ',
           end=NL, file=stdout, flush=False):
    ''' Convert quick_color tags before printing.

        reset_color - send a trailing RESET_ALL string to avoid bleeding '''
    tmp: List[str] = []
    for arg in args:
        tmp.append(quick_color(arg))
    if reset_color:
        tmp.append(RESET_ALL)
    print(*tmp, sep=sep, end=end, file=file, flush=flush)


# # references ...
# colorama_Fore: Dict[str, str] = {
#     'BLACK': '\x1b[30m',
#     'BLUE': '\x1b[34m',
#     'CYAN': '\x1b[36m',
#     'GREEN': '\x1b[32m',
#     'LIGHTBLACK_EX': '\x1b[90m',
#     'LIGHTBLUE_EX': '\x1b[94m',
#     'LIGHTCYAN_EX': '\x1b[96m',
#     'LIGHTGREEN_EX': '\x1b[92m',
#     'LIGHTMAGENTA_EX': '\x1b[95m',
#     'LIGHTRED_EX': '\x1b[91m',
#     'LIGHTWHITE_EX': '\x1b[97m',
#     'LIGHTYELLOW_EX': '\x1b[93m',
#     'MAGENTA': '\x1b[35m',
#     'RED': '\x1b[31m',
#     'RESET': '\x1b[39m',
#     'WHITE': '\x1b[37m',
#     'YELLOW': '\x1b[33m',
# }
# colorama_Back: Dict[str, str] = {
#     'BLACK': '\x1b[40m',
#     'BLUE': '\x1b[44m',
#     'CYAN': '\x1b[46m',
#     'GREEN': '\x1b[42m',
#     'LIGHTBLACK_EX': '\x1b[100m',
#     'LIGHTBLUE_EX': '\x1b[104m',
#     'LIGHTCYAN_EX': '\x1b[106m',
#     'LIGHTGREEN_EX': '\x1b[102m',
#     'LIGHTMAGENTA_EX': '\x1b[105m',
#     'LIGHTRED_EX': '\x1b[101m',
#     'LIGHTWHITE_EX': '\x1b[107m',
#     'LIGHTYELLOW_EX': '\x1b[103m',
#     'MAGENTA': '\x1b[45m',
#     'RED': '\x1b[41m',
#     'RESET': '\x1b[49m',
#     'WHITE': '\x1b[47m',
#     'YELLOW': '\x1b[43m'
# }
# colorama_Style: Dict[str, str] = {
#     'BRIGHT': '\x1b[1m',
#     'DIM': '\x1b[2m',
#     'NORMAL': '\x1b[22m',
#     'RESET_ALL': '\x1b[0m'
# }
