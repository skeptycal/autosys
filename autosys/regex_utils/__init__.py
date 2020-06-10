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

import re
from os import linesep as NL
from dataclasses import dataclass, field, Field
from io import TextIOWrapper
from typing import Final, List

from autosys.exceptions.exceptions import Re_File_Error, Re_Value_Error
from autosys.log.autosys_logger import *

DEFAULT_RE_FLAGS: Final[int] = re.MULTILINE | re.IGNORECASE

# regex pattern to extract version string from text
RE_VERSION: re.Pattern = re.compile(
    pattern=r'^__version__\s?=\s?[\'"]([^\'"]*)[\'"]', flags=DEFAULT_RE_FLAGS,
)

log = logging.getLogger(__name__)
