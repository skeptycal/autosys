#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import

if True: # stdlib imports
    import os
    import pprint
    import sys
    from pathlib import Path
    import ast                      # safer eval ...
    from os import linesep as NL    # platform specific newline
    from os import sep as PATHSEP   # platform specific path separator
    from typing import Dict, List            # >= 3.6 type hints support

if True: # setup tools
    from setuptools import setup, find_packages
    from autosys._version import *

_debug_: bool = False

def readme(filename: str = 'README.md')-> str:
    """ Returns the text of the README file. The default file is `README.md`.

    `readme(filename: str = 'README.md')-> str`

    Example:

    ```
    long_description=readme()
    ```
    """
    readme_path = Path(__file__).resolve().parents[0] / filename

    with open(readme_path, encoding='utf-8') as f:
        return f.read()

class SetupAttrs():
    """ A wrapper for a dictionary of setup attributes.

        Example:

        ```
        from setuptools import setup, find_packages

        s = SetupAttrs()
        print(s) # pretty print attributes

        setup(**s.setup)
        ```
        `Print(s)` will pretty print the attributes.
        """
#? ---------------------- Setup Attributes
    _dict: Dict = {}
    def __init__(self):
        self._dict = {
            'name' : 'autosys',
            'version' : __version__,
            'description' : 'System utilities for Python on macOS',
            'long_description' : readme(),
            'long_description_content_type': 'text/markdown',
            'license' : 'MIT',
            'author' : 'Michael Treanor',
            'author_email' : 'skeptycal@gmail.com',
            'maintainer' : 'Michael Treanor',
            'maintainer_email' : 'skeptycal@gmail.com',
            'url' : f"https://skeptycal.github.io/{__title__}/",
            'python_requires' : '>=3.8',
            # 'cmdclass': '',
            # 'command_options': '',
            # 'command_packages': '',
            # 'data_files': '',
            # 'distclass': '',
            'download_url' : f"https://www.github.com/skeptycal/{__title__}/",
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
            'packages' : find_packages(),
            # 'password' : '',
            # 'platforms': '',
            # 'provides': '',
            # 'py_modules': '',
            # 'requires': '',
            # 'script_args': '',
            # 'script_name' : '',
            # 'scripts': '',
            'zip_safe': False,
            'keywords' : 'application macOS dev cache utilities cli python text console log debug test testing',
            'package_data' : {
                # If any package contains txt, rst, md files, include them:
                "": ["*.txt", "*.rst", "*.md", "*.ini", "*.png", "*.jpg"]
            },
            'project_urls' : {
                "Website": f"https://skeptycal.github.io/{__title__}/",
                "Documentation": f"https://skeptycal.github.io/{__title__}/docs",
                "Source Code": f"https://www.github.com/skeptycal/{__title__}/",
            },
            'classifiers': [
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
#? ---------------------- SetupAttrs Methods

    @property
    def setup(self):
        return self._dict

    def __getitem__(self, name: str):
        return self._dict[name]

    def get(self, name: str):
        return self.__getitem__(name)

    def __str__(self):
        return pprint.pformat(self._dict,depth=5,width=50,compact=False)

s = SetupAttrs()

if _debug_:
    print(f"Running setup for `{s['name']}` version {s['version']}")
    # print(s)
    print(attrs)
else:
    setup(**s.setup)
