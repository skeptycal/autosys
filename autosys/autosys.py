#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" autosys.py """
# copyright (c) 2019 Michael Treanor
# https://www.github.com/skeptycal
# https://www.twitter.com/skeptycal

# `AutoSys` is licensed under the `MIT <https://opensource.org/licenses/MIT>`.

from __future__ import absolute_import, print_function

import os
import sys
from typing import Tuple
import autosys
__version__: str = "1.0.2"
__version_info__: Tuple[int] = (1, 0, 2)
__license__: str = "MIT <https://opensource.org/licenses/MIT>"
__author__: str = "Michael Treanor <skeptycal@gmail.com>"

# from autosys import __version__ as version
# TODO setup a way to automatically track semvers
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('autosys'))

# set default package name to parent folder name
name = __file__.split("/")[-2]
__package__ = name

if __name__ == "__main__":
    # assorted import tests
    import pkgutil
    print()
    print('package name: ', name)
    print()
    print('package version: ', __version__)

    print()
    # print('sys.path: ', sys.path)
    print('builtin modules: ', sys.builtin_module_names)
    print()

    # set to None to see all modules importable from sys.path
    # reference: https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html
    # search_path = None
    # search_path = ['.']
    search_path = ['autosys']
    # search_path = ['as_']
    all_modules = [x[1] for x in pkgutil.iter_modules(path=search_path)]
    print('all importable modules in search_path({}).'.format(search_path))
    print("\n".join(all_modules))
