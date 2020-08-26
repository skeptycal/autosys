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

# logging setup
# Copyright (C) 2012-2019 Vinay Sajip.
# Licensed to the Python Software Foundation under a contributor agreement.

# 'Standard Library'
import logging
import re
import sys

from dataclasses import Field, dataclass, field
from io import TextIOWrapper
from os import environ as ENV, linesep as NL
from sys import argv, path as PYTHON_PATH, stderr, stdout

from typing import Any, Dict, List, NamedTuple, Sequence, Tuple

# 'package imports'
# from autosys.cli.ansi_codes import AnsiCodes
# from autosys.cli.ascii_chars import *
# from autosys.cli.supports_color import SUPPORTS_COLOR
# from autosys.cli.terminal import *



class CommandLineInterfaceException(Exception):
    pass


try:
    from logging import NullHandler
except ImportError:  # pragma: no cover

    class NullHandler(logging.Handler):
        def handle(self, record):
            pass

        def emit(self, record):
            pass

        def createLock(self):
            self.lock = None


logger = logging.getLogger(__name__)
logger.addHandler(NullHandler())
