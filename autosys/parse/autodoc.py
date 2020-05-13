#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" _version.py - version and demographic information

    Part of the `AutoSys` package - utilities for macOS apps
        copyright (c) 2019 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """
from typing import Dict, List
from dataclasses import dataclass

__version_info__ = (0, 4, 4)

__version__ = ".".join(map(str, __version_info__))
__license__: str = "MIT"
__title__: str = "autosys"
__author__: str = "Michael Treanor"
__author_email__: str = "skeptycal@gmail.com"

from datetime import date as _date
from pprint import pprint


# print(dir(_date))
def kv(k, d):
    fmt = f"{d}.{k}()"
    try:
        return eval(f'{fmt}')
    except Exception as e:
        print(f'Error: {e.args[0]:<10.15}. {fmt}')

    fmt = f"{d}.{k}"
    try:
        return eval(fmt)
    except Exception as e:
        print(f'Error: {e.args[0]:<10.15}. {fmt}')

    return 'error'


class ApiSpy():
    src: Dict
    blacklist: List
    whitelist: List
    ''' Get, create, use, evaluate, and document api functionality

        produce a list of outputs from various functions in a module 
        this is basically an automated:
        - an api front end for python modules
        - module tester
        - documentation maker
        - use some simple datetime results to test it


        get keys from dir(module) that are not in blacklist, but are in whitelist
        - use the dunders for info
        - use doc for info
        - search online for documentation
        - try different values until the functions report something feasible

        automating this stuff will help a lot. being able to use modules more automatically would help, and autodocumentation isn't bad either ...

        check keys for values:
        - try calling f(some_default)
        - try calling f()
        - try calling f
        - take a list of inputs to use for f(x) and zip up a dict
        '''
    def __init__(self, d):
        pass
        """ 
        - create a list of functionality
        - identify usual suspects to blacklist
        - default blacklist is starting point
        - identify or input whitelist items ... those will be thoroughly tested and never dropped

        """


_date_dict = {x: kv(x, '_date') for x in dir(_date) if not x.startswith('_')}

# print(_date_dict)

for k, v in _date_dict.items():
    print(f'{k}: {v}\n')


class Now(_date):

    date = _date.today()
    year = date.year

    def __init__(self):

        print(self.year)


# n = Now()


def what_year_is_it():
    from datetime import date
    return str(date.today().year)


def _get_copyright_date(start_year: str = '', _author: str = __author__):
    from datetime import datetime as _dt
    from datetime import date

    date = date.today()
    print(
        f'--- Today is {date:%A}, by the way. If you are working on this code again and the day is Tuesday, you win a cookie.'
    )

    print(what_year_is_it())
    print(what_year_is_it())
    _year: str = str(_dt.now().year)

    if not start_year:
        start_year = _year
    print(f"{_year=} - {type(_year)}")
    print(f"{start_year=} - {type(start_year)}")

    year_fmt: str = f"{_year}"
    if start_year != _year:
        year_fmt = f"{start_year}-{year_fmt}"

    return f'Copyright (c) {year_fmt} {_author}'


__copyright__: str = _get_copyright_date(2018)
__python_requires__: str = ">=3.8"

__all__ = [
    '__version_info__', '__version__', '__license__', '__title__',
    '__author__', '__author_email__', '__copyright__', '__python_requires__'
]

if True:
    from pprint import pprint
    _intro = f'{__title__.title()} setup and version information:'
    _hr = '=' * len(_intro)
    print(_intro)
    print(_hr)
    _fd = {k: eval(k) for k in __all__}
    pprint(_fd)
    # for f in _fields:
    #     print(f"{f} - {eval(f)}")
    #     print('-' * 50)
    print()
    print(f"{__version_info__=}")
    print(f"{__version__=}")
    print(f"{__license__=}")
    print(f"{__title__=}")
    print(f"{__author__=}")
    print(f"{__author_email__=}")
    print(f"{__copyright__=}")
    print(f"{__python_requires__=}")
    print(_hr)
