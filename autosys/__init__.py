#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" autosys package """
# copyright (c) 2019 Michael Treanor
# https://www.github.com/skeptycal/autosys
# https://www.twitter.com/skeptycal

# `AutoSys` is licensed under the `MIT <https://opensource.org/licenses/MIT>`.
from __future__ import absolute_import, print_function
from autosys import *


if True:  # import builtins
    import decimal
    import fileinput
    import inspect
    import locale
    import logging
    import math
    import os
    import sys
    import textwrap
    import time
    import timeit
    import traceback

if True:  # other imports
    from typing import Any, Dict, FrozenSet, List, Sequence, Tuple

if True:  # designed to be run globally from directory in system path
    # the sys.path starts with the directory containing __file__ which we want to remove as
    # that dir might be anywhere and could contain anything; it's not needed for locating
    # autosys modules since those will be in site-packages once autosys is installed
    script_path = os.path.abspath(sys.path[0])
    sys.path = [p for p in sys.path if os.path.abspath(p) != script_path]
    # opposite of:
    # sys.path.insert(0, os.path.abspath("."))  # insert pwd
    # sys.path.insert(0, os.path.abspath('autosys'))

if True:  # package defaults
    # TODO setup a way to automatically track semvers
    __version__: str = "1.0.2"
    version: str = __version__
    __version_info__: Tuple[int] = (int(_) for _ in version.split('.'))

    # set default package name to parent folder name
    name: str = __file__.split("/")[-2]
    __package__: str = name

    __license__: str = "MIT <https://opensource.org/licenses/MIT>"
    __author__: str = "Michael Treanor <skeptycal@gmail.com>"


if __name__ == "__main__":  # CLI tests
    # assorted import tests
    import pkgutil
    print()
    print('package name: ', name)
    print()
    print('package version: ', __version__)

    # print(dir(sys))
    print()
    # print('sys.path: ', sys.path)
    print()
    print('builtin modules: ', sys.builtin_module_names)
    print()

    # set to None to see all modules importable from sys.path
    # reference: https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html
    # search_path = None
    # search_path = ['.']
    search_path = ['autosys']
    all_modules = [x[1] for x in pkgutil.iter_modules(path=search_path)]
    print('all importable modules in search_path({}).'.format(search_path))
    print("\n".join(all_modules))
    print(PY_VER)
