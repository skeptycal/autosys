#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" AutoSys Package Metadata
    ---
    Part of the [AutoSys][1] package

    Copyright (c) 2018 [Michael Treanor][2]

    AutoSys is licensed under the [MIT License][3]

    [1]: https://www.github.com/skeptycal/autosys
    [2]: https://www.twitter.com/skeptycal
    [3]: https://opensource.org/licenses/MIT
    """

from setup import pip_safe_name, readme

from typing import Dict, List, Tuple

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
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Software Development :: Testing",
    "Topic :: Utilities",
]
