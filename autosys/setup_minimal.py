#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minimal Python Module Setup File
Requires Python 3.7 (dataclass support)
"""
from dataclasses import asdict, astuple, dataclass, field
from typing import Any, Dict, List, Tuple

from setuptools import setup

# set default package name to parent folder name


@dataclass(frozen=True)
class SetupConfig:
    # __slots__ = ['name', 'version', 'description', 'url',
    #              'author', 'author_email', 'license', 'packages', 'zip_safe']

    name: str = __file__.split("/")[-2]
    version: str = "0.0.1"
    description: str = "a utility for macOS"
    url: str = "http://github.com/skeptycal/" + name
    author: str = "Michael Treanor"
    author_email: str = "skeptycal@gmail.com"
    license: str = "MIT"
    # packages = []
    zip_safe: bool = False

    def __post_init__(self):
        pass

    def __iter__(self):
        yield from asdict(self)

    def __str__(self):
        return f"{self.name.capitalize()} version {self.version} - {self.description}."


if __name__ == "__main__":

    s = SetupConfig(version="0.1")

    s_iter = iter(s)
    print()
    print(s)
    print()
    print(str(s.__repr__()))
    print()
    print((s.__getattribute__("name")))
    print()
    for k in iter(s):
        print(k, ": ", s.__getattribute__(k))
    print({str(k) + ": " + str(s.__getattribute__(k)) for k in iter(s)})
    # s_dict = dict(iter(s))
    # print(s_dict)
    # print()
    print()
