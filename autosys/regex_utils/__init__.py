#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Logger
    ---
    logger - A wrapper class to setup common logging functions.

    AutoSys
    ---
    Part of the [AutoSys][1] package

    Copyright (c) 2018 [Michael Treanor][2]

    AutoSys is licensed under the [MIT License][3]

    [1]: https://www.github.com/skeptycal/autosys
    [2]: https://www.twitter.com/skeptycal
    [3]: https://opensource.org/licenses/MIT
    """

# 'Standard Library'
import re

from dataclasses import (
    Field,
    dataclass,
    field,
)
from io import TextIOWrapper
from os import linesep as NL
from pathlib import Path

# 'package imports'
from autosys.exceptions.exceptions import (
    Re_File_Error,
    Re_Value_Error,
)
from autosys.forks import logging

from typing import (
    Final,
    List,
)

DEFAULT_RE_FLAGS: Final[int] = re.MULTILINE | re.IGNORECASE

# regex pattern to extract version string from text
RE_VERSION: re.Pattern = re.compile(
    pattern=r'^__version__\s?=\s?[\'"]([^\'"]*)[\'"]',
    flags=DEFAULT_RE_FLAGS,
)

log = logging.getLogger(__name__)
