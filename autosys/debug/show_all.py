#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" `AutoSys` package
        copyright (c) 2018 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """

_blacklist = [
    "Field",
    "Final",
    "List",
    "arepl_store",
    "choice",
    "help",
    "howdoi",
    "input",
    "linesep",
    "show_all",
    "Tuple",
    "dataclass",
    "field",
]


def show_all(x):
    print("__all__: List[str] = [")
    for i in x:
        if i.startswith("_"):
            continue
        if i in _blacklist:
            continue
        print(f"    '{i}',")
    print("]")
