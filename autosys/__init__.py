#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# `AutoSys` is licensed under the `MIT <https://opensource.org/licenses/MIT>`.

from __future__ import absolute_import, print_function

__version__ = "1.0.2"
__version_info__ = (1, 0, 2)
__license__ = "MIT <https://opensource.org/licenses/MIT>"
__author__ = "Michael Treanor <skeptycal@gmail.com>"

import sys
import os


# from autosys import __version__ as version
sys.path.insert(0, os.path.abspath('.'))
# TODO setup a way to automatically track semvers

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
    urls = ['http://www.google.com', 'https://www.google.com',
            'https://www.twitter.com/skeptycal']
    # 'https://www.skeptycal.com'
    for url in urls:
        res = url_test(url)
        print()
        if res == 200:
            print(f'Successful connection to {url} ...response: {res}')
        else:
            print(f'No connection to {url} ... response: {res}')
