#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minimal Python Module Setup File
Requires Python 3.7 (dataclass support)
"""
# 'future imports'
from __future__ import absolute_import, print_function

# 'Standard Library'
from dataclasses import asdict, astuple, dataclass, field

# 'third party'
from setuptools import setup

from typing import Any, Dict, List, Tuple

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
    pass
