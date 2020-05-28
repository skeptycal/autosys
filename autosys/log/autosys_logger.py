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

from pathlib import Path
from sys import argv
from tempfile import NamedTemporaryFile
from locale import getpreferredencoding
from typing import Dict, Final, List, Tuple
from io import TextIOWrapper
from logging import Logger as _Logger

print(dir(_Logger))


class Logger(_Logger):
    def fmt_info(self):
        pass


log = Logger(__file__)
