#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import

if True:  # stdlib imports
    import ast  # safer eval ...
    import os  # basic OS features
    import pprint  # pretty printing
    import sys  # basic system features
    from pathlib import Path  # path features
    from os import linesep as NL, sep as PATHSEP
    from typing import Dict, List  # >= 3.6 type hints support

if True:  # setup tools
    from setuptools import setup, find_packages
    from autosys._version import *

_debug_: bool = False


def readme(filename: str = "README.md"):
    """ Returns the text of the README file. The default file is `README.md`.

    `readme(filename: str = 'README.md')-> str`

    Example:

    ```
    long_description=readme()
    ```
    """
    readme_path = Path(__file__).resolve().parents[0] / filename

    with open(readme_path, encoding="utf-8") as f:
        return f.read()


class SetupAttrs:
    """ A wrapper for a dictionary of setup attributes.

        Example:

        ```
        from setuptools import setup, find_packages

        s = SetupAttrs()
        print(s) # pretty print attributes

        setup(**s.setup)
        ```
        `Print(s)` will pretty print the attributes.
        
        The following data are imported from ./<package_name>/_version.py
        
            __version__: str = "x.x.x"
            __license__: str = "MIT"
            __title__: str = "xxxxx"
            __author__: str = "xxxxx xxxxx"
            __copyright__: str = f"Copyright (c) xxxx xxxxx xxxxx"
            __author_email__: str = "xxx@xxx.com"
            __python_requires__: str = ">=x.x"
        """

    # ? ---------------------- SetupAttrs Attributes
    _dict: Dict = {}

    def __init__(self):
        self._version = __version__
        self._license = __license__
        self._title = __title__
        self._copyright = __copyright__
        self._author = __author__
        self._author_email = __author_email__
        self._python_requires = __python_requires__
        self.load_dict()

    def load_dict(self):
        self._dict = {
            "name": self._title,
            "version": self._version,
            "description": "System utilities for Python on macOS",
            "long_description": readme(),
            "long_description_content_type": "text/markdown",
            "license": self._license,
            "author": self._author,
            "author_email": self._author_email,
            "maintainer": self._author,
            "maintainer_email": self._author_email,
            "url": f"https://skeptycal.github.io/{__title__}/",
            "python_requires": self._python_requires,
            # 'cmdclass': '',
            # 'command_options': '',
            # 'command_packages': '',
            # 'data_files': '',
            # 'distclass': '',
            "download_url": f"https://www.github.com/skeptycal/{__title__}/",
            # 'ext_modules': '',
            # 'ext_package' : '',
            # 'fullname' : '',
            # 'headers': '',
            # 'include_dirs': '',
            # 'include_package_data': '',
            # 'libraries': '',
            # 'obsoletes': '',
            # 'options': '',
            # 'package_data': '',
            # 'package_dir' : {'': __title__},
            # 'package_dir': '',
            # 'packages': '',
            "packages": find_packages(),
            # 'password' : '',
            # 'platforms': '',
            # 'provides': '',
            # 'py_modules': '',
            # 'requires': '',
            # 'script_args': '',
            # 'script_name' : '',
            # 'scripts': '',
            "zip_safe": False,
            "keywords": "application macOS dev cache utilities cli python text console log debug test testing",
            "package_data": {
                # If any package contains txt, rst, md files, include them:
                "": ["*.txt", "*.rst", "*.md", "*.ini", "*.png", "*.jpg"]
            },
            "project_urls": {
                "Website": f"https://skeptycal.github.io/{__title__}/",
                "Documentation": f"https://skeptycal.github.io/{__title__}/docs",
                "Source Code": f"https://www.github.com/skeptycal/{__title__}/",
            },
            "classifiers": [
                "Development Status :: 4 - Beta",
                "Environment :: Console",
                "Environment :: MacOS X",
                "Intended Audience :: Developers",
                "License :: OSI Approved :: MIT License",
                "Natural Language :: English",
                "Operating System :: MacOS",
                "Programming Language :: Cython",
                "Programming Language :: Python",
                "Programming Language :: Python :: 3.8",
                "Programming Language :: Python :: Implementation :: CPython",
                "Programming Language :: Python :: Implementation :: PyPy",
                "Topic :: Software Development :: Libraries :: Python Modules",
                "Topic :: Software Development :: Testing",
                "Topic :: Utilities",
            ],
        }

    # ? ---------------------- SetupAttrs Properties
    @property
    def setup(self):
        return self._dict

    @property
    def version(self):
        return self._version

    @property
    def author(self):
        return self._author

    @property
    def email(self):
        return self._author_email

    @property
    def title(self):
        return self._title

    @property
    def license(self):
        return self._license

    # ? ---------------------- SetupAttrs Methods
    def __getitem__(self, name: str):
        return self._dict[name]

    def get(self, name: str):
        return self.__getitem__(name)

    def __str__(self):
        return pprint.pformat(self._dict, depth=5, compact=False)


s = SetupAttrs()

if _debug_:
    print(f"Debug mode: setup for `{s['name']}` version {s['version']}")
    print()
    print(s.license)
    print(s)
else:
    setup(**s.setup)
