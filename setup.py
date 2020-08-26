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

from os import linesep as NL
from pathlib import Path
from sys import argv as _argv, path as PYTHONPATH

from setuptools import find_namespace_packages, setup

from typing import Dict, Final, List, Optional, Sequence, Tuple

# ? #################################### config

try:
    DEFAULT_ENCODING
except:
    from locale import getpreferredencoding
    DEFAULT_ENCODING: str = getpreferredencoding(do_setlocale=True) or "utf-8"

#! DEBUG - run some live tests ... set 'False' for production !!!
_debug_: bool = False


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


# ? #################################### package metadata.
__version__: str = '0.4.4'


NAME: str = pip_safe_name("AutoSys")

VERSION: str = __version__  # "0.4.4"
VERSION_INFO: Tuple[int] = VERSION.split(".")
DESCRIPTION: str = "System utilities for Python on macOS."
REQUIRES_PYTHON: str = ">=3.8.0"
PACKAGE_DIR: Dict = {'': f'{NAME}'}
PACKAGE_EXCLUDE: List[str] = ['*test*', '*bak*']
LICENSE: str = "MIT"
LONG_DESCRIPTION: str = readme()
LONG_DESCRIPTION_CONTENT_TYPE: str = "text/markdown"
# LONG_DESCRIPTION_CONTENT_TYPE="text/x-rst",
AUTHOR: str = "Michael Treanor"
AUTHOR_EMAIL: str = "skeptycal@gmail.com"
MAINTAINER: str = ""
MAINTAINER_EMAIL: str = ""
URL: str = f"https://skeptycal.github.io/{NAME}/"
DOWNLOAD_URL: str = f"https://github.com/skeptycal/{NAME}/archive/{VERSION}.tar.gz"
ZIP_SAFE: bool = False
INCLUDE_PACKAGE_DATA: bool = True
# What packages are required for this module to be executed?
REQUIRED: List[str] = [
    "aiocontextvars>=0.2.0 ; python_version<'3.7'",
    "colorama>=0.3.4 ; sys_platform=='win32'",
    "win32-setctime>=1.0.0 ; sys_platform=='win32'",
]

# What packages are optional?
EXTRAS: Dict = {
    ":python_version < '3.5'": ["typing==3.6.1", ],
    "dev": [
        "black>=19.3b0 ; python_version>='3.8'",
        "codecov>=2.0.15",
        "flake8>=3.7.7",
        "isort>=4.3.20",
        "tox>=3.9.0",
        "tox-travis>=0.12",
        "pytest>=4.6.2",
        "pytest-cov>=2.7.1",
        "Sphinx>=2.2.1",
        "sphinx-autobuild>=0.7.1",
        "sphinx-rtd-theme>=0.4.3",
    ]
}

PACKAGE_DATA: Dict = {
    # If any package contains these files, include them:
    "": [
        "*.txt",
        "*.rst",
        "*.md",
        "*.ini",
        "*.png",
        "*.jpg",
        "*.py",
        "__init__.pyi",
        "py.typed",
    ]
}

PROJECT_URLS: Dict = {
    "Website": f"https://skeptycal.github.io/{NAME}/",
    "Documentation": f"https://skeptycal.github.io/{NAME}/docs",
    "Source Code": f"https://www.github.com/skeptycal/{NAME}/",
    "Changelog":
    f"https://github.com/skeptycal/{NAME}/blob/master/CHANGELOG.md",
}

KEYWORDS: List = [
    "application",
    "macOS",
    "dev",
    "devops",
    "cache",
    "utilities",
    "cli",
    "python",
    "cython",
    "text",
    "console",
    "log",
    "debug",
    "test",
    "testing",
    "logging",
    "logger",
]
CLASSIFIERS: List = [
    "Development Status :: 4 - Beta",
    "License :: OSI Approved :: MIT License",
    "Environment :: Console",
    "Environment :: MacOS X",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "Operating System :: MacOS",
    "Operating System :: OS Independent",
    "Programming Language :: Cython",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3",
    # These are the Python versions tested; it may work on others
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Software Development :: Testing",
    "Topic :: Utilities",
]


def main(args=_argv[1:], ):  # ? ############################## Setup!
    global _debug_
    if 'debug' in args:
        _debug_ = True
    if _debug_:  # do some live tests if setup process has changed ...
        print(f"{NAME=}")
        print(f"{VERSION=}")
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
    pass
    '''
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
    '''
