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
from dataclasses import dataclass
from datetime import date as _date
from pprint import pprint
from typing import Dict, List


# print(dir(_date))
def kv(k, d):
    fmt = f"{d}.{k}()"
    try:
        return eval(f"{fmt}")
    except Exception as e:
        print(f"Error: {e.args[0]:<10.15}. {fmt}")

    fmt = f"{d}.{k}"
    try:
        return eval(fmt)
    except Exception as e:
        print(f"Error: {e.args[0]:<10.15}. {fmt}")

    return "error"


class ApiSpy:
    src: Dict
    blacklist: List
    whitelist: List
    """ Get, create, use, evaluate, and document api functionality

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
        """

    def __init__(self, d):
        pass
        """
        - create a list of functionality
        - identify usual suspects to blacklist
        - default blacklist is starting point
        - identify or input whitelist items ... those will be thoroughly tested and never dropped

        """


_date_dict = {x: kv(x, "_date") for x in dir(_date) if not x.startswith("_")}

# print(_date_dict)

for k, v in _date_dict.items():
    print(f"{k}: {v}\n")


class Now(_date):

    date = _date.today()
    year = date.year

    def __init__(self):

        print(self.year)


# n = Now()


def what_year_is_it():
    from datetime import date

    return str(date.today().year)


if True:
    from pprint import pprint

    _intro = f"{__title__.title()} setup and version information:"
    _hr = "=" * len(_intro)
    print(_intro)
    print(_hr)
    _fd = {k: eval(k) for k in __all__}
    pprint(_fd)
    # for f in _fields:
    #     print(f"{f} - {eval(f)}")
    #     print('-' * 50)
    print()

    print(_hr)
