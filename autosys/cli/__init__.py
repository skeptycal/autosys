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

import logging
import re
import sys
from sys import argv, stderr, stdout, path as PYTHON_PATH
from platform import platform
from os import environ as ENV, linesep as NL
from io import TextIOWrapper
from dataclasses import Field, dataclass, field
from typing import Any, Dict, List, NamedTuple, Sequence, Tuple

from autosys.cli.terminal import *
from autosys.cli.ansi_codes import AnsiCodes
from autosys.cli.ascii_chars import *
from autosys.cli.supports_color import SUPPORTS_COLOR

PLATFORM = platform()


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
