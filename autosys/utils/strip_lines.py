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
from logging import Logger


class FileSet(list):
    input_list: List[str]
    temp_file: TextIOWrapper
    log: Logger

    def __init__(self, *args):
        self.input_list = args
        self.temp_file = NamedTemporaryFile(mode="wt", prefix=__file__)
        self.log = Logger(__file__)

    def __str__(self):
        return self.lines

    def txt_replace(self, needle, haystack):
        pass

    def drop_lines(self):
        for original in files:
            with NamedTemporaryFile(mode="wt", prefix=__file__,) as temp_file:
                with open(
                    file=original, mode="rt", encoding=self.DEFAULT_ENCODING
                ) as fd:
                    data = fd.readlines()

                # process lines

                with open(file=f""):
                    pass

                Path(temp_filename).replace(original_filename)
