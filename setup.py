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

import os
import re

from dataclasses import Field, dataclass, field
from os import linesep as NL
from pathlib import Path
from shutil import rmtree as _rmtree
from sys import argv as _argv, path as PYTHONPATH

# from autosys.regex_utils.re_extract import *
# from autosys.utils.readme import readme

from setuptools import find_namespace_packages, setup

from typing import Dict, Final, List, Optional, Tuple

try:
    DEFAULT_ENCODING
except:
    from locale import getpreferredencoding
    DEFAULT_ENCODING: str = getpreferredencoding(do_setlocale=True) or "utf-8"


#! DEBUG - run some live tests ... set 'False' for production !!!
_debug_: bool = False
here = Path(__file__).resolve().parent
# print(here)
if here not in PYTHONPATH:
    PYTHONPATH.insert(0, here)
    PYTHONPATH.append(here)

# log = logging.getLogger(__name__)

__version__ = '0.4.4'

# ? #################################### packaging utilities.


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


# ? #################################### package meta-data.
NAME: str = pip_safe_name("AutoSys")

VERSION: str = __version__  # "0.4.4"
VERSION_INFO: Tuple[int] = VERSION.split(".")
DESCRIPTION: str = "System utilities for Python on macOS."
EMAIL: str = "skeptycal@gmail.com"
AUTHOR: str = "Michael Treanor"
LICENSE: str = "MIT"
REQUIRES_PYTHON: str = ">=3.8.0"
MAINTAINER: str = ""
MAINTAINER_EMAIL: str = ""
LONG_DESCRIPTION_CONTENT_TYPE = "text/markdown"
# long_description_content_type="text/x-rst",
URL = f"https://skeptycal.github.io/{NAME}/"
DOWNLOAD_URL = f"https://github.com/skeptycal/{NAME}/archive/{VERSION}.tar.gz"

# What packages are required for this module to be executed?
REQUIRED = [
    "aiocontextvars>=0.2.0 ; python_version<'3.7'",
    "colorama>=0.3.4 ; sys_platform=='win32'",
    "win32-setctime>=1.0.0 ; sys_platform=='win32'",
]

# What packages are optional?
EXTRAS = {
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

PACKAGE_DATA = {
    # If any package contains these files, include them:
    "": [
        "*.txt",
        "*.rst",
        "*.md",
        "*.ini",
        "*.png",
        "*.jpg",
        "__init__.pyi",
        "py.typed",
    ]
}

PROJECT_URLS = {
    "Website": f"https://skeptycal.github.io/{NAME}/",
    "Documentation": f"https://skeptycal.github.io/{NAME}/docs",
    "Source Code": f"https://www.github.com/skeptycal/{NAME}/",
    "Changelog":
    f"https://github.com/skeptycal/{NAME}/blob/master/CHANGELOG.md",
}

KEYWORDS = [
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
CLASSIFIERS = [
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
    if _debug_:  # do some live tests if setup process has changed ...
        print(f"{NAME=}")
        print(f"{version=}")
        print(f"{type(version)=}")
        print(f"{VERSION=}")

    else:  # run setup ...
        setup(
            name=NAME,
            version=VERSION,
            description=DESCRIPTION,
            python_requires=REQUIRES_PYTHON,
            packages=find_namespace_packages(),
            # py_modules=[f"{NAME}"],
            license=LICENSE,
            long_description=readme(),
            long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
            author=AUTHOR,
            author_email=EMAIL,
            maintainer=MAINTAINER or AUTHOR,
            maintainer_email=MAINTAINER_EMAIL or EMAIL,
            keywords=KEYWORDS,
            url=URL,
            download_url=DOWNLOAD_URL,
            zip_safe=False,
            include_package_data=True,
            # setup_requires=["isort"],
            package_data=PACKAGE_DATA,
            project_urls=PROJECT_URLS,
            install_requires=REQUIRED,
            extras_require=EXTRAS,
            classifiers=CLASSIFIERS,
        )


_vars = vars()
if __name__ == "__main__":
    main()
