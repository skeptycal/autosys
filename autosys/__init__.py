# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import sys
import os

# from autosys import __version__ as version
sys.path.insert(0, os.path.abspath('.'))
# TODO setup a way to automatically track semvers
__version__ = "1.0.2"

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

    # print(dir(sys))
    print()
    print('sys.path: ', sys.path)
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
    print()
