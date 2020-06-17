#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" AutoSys Setup
    ---
    Part of the [AutoSys][1] package

    Copyright (c) 2018 [Michael Treanor][2]

    AutoSys is licensed under the [MIT License][3]

    [1]: https://www.github.com/skeptycal/autosys
    [2]: https://www.twitter.com/skeptycal
    [3]: https://opensource.org/licenses/MIT
    """

# Note: To use the 'upload' functionality of this file, you must:
#   $ pip install twine

import logging
import os
import re

# from dataclasses import Field, dataclass, field
from os import linesep as NL
from pathlib import Path
# from shutil import rmtree as _rmtree
from sys import stdout, argv as _argv, path as PYTHONPATH

from package_metadata import *

from colorama import Back, Fore, Style
from setuptools import find_namespace_packages, setup
from functools import lru_cache

from typing import Dict, Final, List, Optional, Sequence, Tuple


try:
    DEFAULT_ENCODING
except:
    from locale import getpreferredencoding
    DEFAULT_ENCODING: str = getpreferredencoding(do_setlocale=True) or "utf-8"

#! DEBUG - run some live tests ... set 'False' for production !!!
_debug_: bool = True


here = Path(__file__).resolve().parent

if here not in PYTHONPATH:
    PYTHONPATH.insert(0, here)

logger = logging.getLogger(__name__)


# ? #################################### packaging utilities.
def table_print(data: (Dict, Sequence), **kwargs):
    tmp: List = []
    if isinstance(data, dict):
        tmp.extend(
            [f"{str(k):<15.15} :  {repr(v):<45.45}" for k, v in data.items()])
    elif isinstance(data, (list, tuple, set)):
        for x in data:
            try:
                tmp.append(f"{str(x):<15.15} :  {repr(f'{x}'):<45.45}")
            except:
                tmp.append(f"{str(x)}")
    else:
        raise TypeError('Parameter must be an iterable Mapping or Sequence.')
    print(NL.join(tmp), **kwargs)


def pip_safe_name(s: str):
    """ Return a name that is converted to pypi safe format. """
    return s.lower().replace("-", "_").replace(" ", "_")


def readme(file_name: str = "readme.md"):
    """ Returns the text of the README file

        The default file is `README.md` and is *NOT* case sensitive. (e.g. `README` is the same as `readme`)
        Can load *any* text file, but the default search path is setup for readme files

        ```
        Search path = ["readme.md", "readme.rst", "readme", "readme.txt"]
        ```

        Example:

        ```
        long_description=readme()
        ```
        """

    search_list = ["readme.md", "readme.rst", "readme", "readme.txt"]
    if file_name not in search_list:
        search_list.insert(0, file_name)
    found: bool = False
    for searchfile in search_list:
        for parent in Path(__file__).resolve().parents:
            find_path = Path(parent / searchfile)
            if find_path.exists():
                found = True
                # print(find_path)
                break
        if found:
            break
    if found:
        try:
            with open(find_path, mode="r", encoding=DEFAULT_ENCODING) as f:
                return f.read()
        except IOError as e:
            raise IOError(f"Cannot read from the 'readme' file '{find_path}'")
    else:
        raise FileNotFoundError(
            f"Cannot find project 'readme' file in project tree. Search list = {search_list}"
        )


quick_colors: Dict[str, str] = {
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
    '<k>': '\x1b[30m',  # lowercase ...
    '<b>': '\x1b[34m',
    '<c>': '\x1b[36m',
    '<g>': '\x1b[32m',
    '<m>': '\x1b[35m',
    '<r>': '\x1b[31m',
    '<w>': '\x1b[37m',
    '<y>': '\x1b[33m',
    '<lk>': '\x1b[90m',  # lowercase light colors
    '<lb>': '\x1b[94m',
    '<lc>': '\x1b[96m',
    '<lg>': '\x1b[92m',
    '<lm>': '\x1b[95m',
    '<lr>': '\x1b[91m',
    '<lw>': '\x1b[97m',
    '<ly>': '\x1b[93m',
    '<x>': '\x1b[39m',  # x is for reset
    '<X>': '\x1b[39m',  # X is for reset
}

RE_QUICK_COLOR_TAG: re.Pattern = re.compile(r'<\w{1,2}>')
RESET_ALL = '\x1b[0m'


def re_quick_color(s: str) -> (re.Match, None):
    ''' return the next regex match or None'''
    try:
        return re.search(RE_QUICK_COLOR_TAG, s)[0]
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
def qprint(*args, reset_color=True, sep=' ',  end=NL, file=stdout, flush=False):
    tmp: List[str] = []
    for arg in args:
        tmp.append(quick_color(arg))
    if reset_color:
        tmp.append(RESET_ALL)
    print(*tmp, sep=sep, end=end, file=file, flush=flush)


_vars = vars()


def main(args=_argv[1:], ):  # ? ############################## Setup!
    print(f"{Fore.YELLOW}setup for '{Fore.GREEN}{NAME}{Fore.YELLOW}' version {Fore.RED}{VERSION}{Fore.RESET}")
    global _debug_
    if 'debug' in args:
        _debug_ = True
    if _debug_:  # do some live tests if setup process has changed ...
        pass
        print(f"{NAME=}")
        print(f"{VERSION=}")
        qprint("<b>Blue <r>Red")
        # table_print(_vars)
    else:  # run setup ...
        setup(
            name=NAME,
            version=VERSION,
            description=DESCRIPTION,
            python_requires=REQUIRES_PYTHON,
            package_dir=PACKAGE_DIR,
            packages=find_namespace_packages(
                f'{NAME}', exclude=PACKAGE_EXCLUDE),
            # py_modules=[f"{NAME}"],
            license=LICENSE,
            long_description=LONG_DESCRIPTION,
            long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
            author=AUTHOR,
            author_email=AUTHOR_EMAIL,
            maintainer=MAINTAINER or AUTHOR,
            maintainer_email=MAINTAINER_EMAIL or AUTHOR_EMAIL,
            url=URL,
            download_url=DOWNLOAD_URL,
            zip_safe=ZIP_SAFE,
            include_package_data=INCLUDE_PACKAGE_DATA,
            # setup_requires=["isort"],
            install_requires=REQUIRED,
            extras_require=EXTRAS,
            package_data=PACKAGE_DATA,
            project_urls=PROJECT_URLS,
            keywords=KEYWORDS,
            classifiers=CLASSIFIERS,
        )


if __name__ == "__main__":
    main()

else:
    # references ...
    colorama_Fore: Dict[str, str] = {
        'BLACK': '\x1b[30m',
        'BLUE': '\x1b[34m',
        'CYAN': '\x1b[36m',
        'GREEN': '\x1b[32m',
        'LIGHTBLACK_EX': '\x1b[90m',
        'LIGHTBLUE_EX': '\x1b[94m',
        'LIGHTCYAN_EX': '\x1b[96m',
        'LIGHTGREEN_EX': '\x1b[92m',
        'LIGHTMAGENTA_EX': '\x1b[95m',
        'LIGHTRED_EX': '\x1b[91m',
        'LIGHTWHITE_EX': '\x1b[97m',
        'LIGHTYELLOW_EX': '\x1b[93m',
        'MAGENTA': '\x1b[35m',
        'RED': '\x1b[31m',
        'RESET': '\x1b[39m',
        'WHITE': '\x1b[37m',
        'YELLOW': '\x1b[33m',
    }
    colorama_Back: Dict[str, str] = {
        'BLACK': '\x1b[40m',
        'BLUE': '\x1b[44m',
        'CYAN': '\x1b[46m',
        'GREEN': '\x1b[42m',
        'LIGHTBLACK_EX': '\x1b[100m',
        'LIGHTBLUE_EX': '\x1b[104m',
        'LIGHTCYAN_EX': '\x1b[106m',
        'LIGHTGREEN_EX': '\x1b[102m',
        'LIGHTMAGENTA_EX': '\x1b[105m',
        'LIGHTRED_EX': '\x1b[101m',
        'LIGHTWHITE_EX': '\x1b[107m',
        'LIGHTYELLOW_EX': '\x1b[103m',
        'MAGENTA': '\x1b[45m',
        'RED': '\x1b[41m',
        'RESET': '\x1b[49m',
        'WHITE': '\x1b[47m',
        'YELLOW': '\x1b[43m'
    }
    colorama_Style: Dict[str, str] = {
        'BRIGHT': '\x1b[1m',
        'DIM': '\x1b[2m',
        'NORMAL': '\x1b[22m',
        'RESET_ALL': '\x1b[0m'
    }
