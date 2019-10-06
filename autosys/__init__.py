#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" autosys package """
# copyright (c) 2019 Michael Treanor
# https://www.github.com/skeptycal/autosys
# https://www.twitter.com/skeptycal

# `AutoSys` is licensed under the `MIT <https://opensource.org/licenses/MIT>`.
# from __future__ import absolute_import, print_function
# from autosys import *

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
    __version_info__: Tuple[int] = [int(_) for _ in version.split('.')]

    # set default package name to parent folder name
    name: str = __file__.split("/")[-2]
    __package__: str = name

    __license__: str = "MIT <https://opensource.org/licenses/MIT>"
    __author__: str = "Michael Treanor <https://www.github.com/skeptycal>"

if __name__ == "__main__":  # CLI tests
    # assorted import tests
    import pkgutil
    from autosys.as_system import njoin
    from autosys.as_constants import PY_ENV

    MAIN = PY_ENV.get('MAIN')
    CANARY = PY_ENV.get("CANARY")
    RESET = PY_ENV.get("RESET_FG")

    def v_name(the_var: Any) -> str:
        try:
            result = [
                var_name for var_name, var_val in
                inspect.currentframe().f_back.f_back.f_locals.items()
                if var_val is the_var
            ][0]
            return result
        except IndexError as e:
            return ''

    def vprint(the_var: Any):
        print(f'{MAIN}{v_name(the_var)} => {CANARY}{the_var}{RESET}')

    def cprint(s: str):
        print(f'{MAIN}{s}{RESET}')

    print()
    cprint('dir(pkgutil)')
    print(dir(pkgutil))

    print()
    cprint('builtin modules: ')
    print(njoin(sys.builtin_module_names))
    print()

    # set to None to see all modules importable from sys.path
    # reference: https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html
    # search_path = None
    # search_path = ['.']
    search_path = ['autosys']
    cprint(f'all importable modules in search_path({search_path}).')
    all_modules = [x[1] for x in pkgutil.iter_modules(path=search_path)]
    print(njoin(all_modules))

    print()
    vprint(license)

    print()
    cprint("Test Values")
    cprint("*" * 40)
    vprint(name)
    vprint(__author__)
    vprint(__license__)
    vprint(__version__)
    vprint(__version_info__)
