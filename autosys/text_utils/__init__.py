#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Common imports, CONSTANTS, and utilities for the `AutoSys` package

    Part of the `AutoSys` package - utilities for macOS apps
        copyright (c) 2019 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """

import dataclasses
import json
import os
import string
from dataclasses import Field, dataclass, field
from os import linesep as NL
from typing import Dict, List

NUL: str = chr(0)

STR_ALPHA: str = string.ascii_letters
STR_ALPHANUMERIC: str = string.ascii_letters + string.digits
STR_HEX: str = string.hexdigits
STR_NAMES: str = string.ascii_letters + " _-"
STR_WHITESPACE: str = string.whitespace
STR_PRINTABLE: str = string.printable
STR_PUNCTUATION: str = string.punctuation
