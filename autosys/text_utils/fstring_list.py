#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 'Standard Library'
from dataclasses import dataclass
from enum import (
    Enum,
    IntEnum,
    unique,
)
from time import sleep

# 'package imports'
from autosys import *
from cli.supports_color import SUPPORTS_COLOR

# 'third party'
import numpy as np

from typing import (
    Dict,
    Iterable,
)

NAN = object()
NUL = ""

'''
@unique
class NpAlign(Enum):
    left = "<"
    right = ">"
    center = "^"


@unique
class FB(Enum):
    fg = 3
    bg = 4


class Code8:
    black: str = "0"
    red: str = "1"
    green: str = "2"
    yellow: str = "3"
    blue: str = "4"
    magenta: str = "5"
    cyan: str = "6"
    white: str = "7"


class Code16:
    black: str = "0"
    red: str = "1"
    green: str = "2"
    yellow: str = "3"
    blue: str = "4"
    magenta: str = "5"
    cyan: str = "6"
    white: str = "7"
    bright_black: str = "0;1"
    bright_red: str = "1;1"
    bright_green: str = "2;1"
    bright_yellow: str = "3;1"
    bright_blue: str = "4;1"
    bright_magenta: str = "5;1"
    bright_cyan: str = "6;1"
    bright_white: str = "7;1"


class Effects:
    bold: str = "\u001b[1m"
    underline: str = "\u001b[4m"
    reverse: str = "\u001b[7m"
    reset: str = "\u001b[0m"


class Ansi(str):
    reset: str = "\u001b[0m"

    def __init__(self, *args, **kwargs):
        super(*args, **kwargs)

    def _color8(self, c: Code8 = "1", fb: FB = FB.fg):
        """ get either fg or bg color (8) - default fg """
        return f"{self}\u001b[{fb}{c}m"

    def _color16(self, c: Code16 = Code16.blue, fb: FB = FB.fg):
        """ get either fg or bg color (16) - default fg """
        return f"{self}\u001b[{fb}{c}m"

    def _color256(self, c="229", fb: FB = FB.fg):
        """ get either fg or bg color (256) - default fg """
        return f"\u001b[{fb}8;5;{c}m"

    def fb(self, fg="0", bg="229"):
        """ <F>oreground / <B>ackground 256 color combo """
        return f"\u001b[38;5;{fg}m\u001b[48;5;{bg}m"


class ColorToggle:
    a = Ansi()
    DEFAULT_NORMAL = a.fb(fg=2, bg=229)
    DEFAULT_REVERSE = a.fb(fg=16, bg=229)

    reset: str = "\u001b[0m"

    def __init__(
        self,
        norm=DEFAULT_NORMAL,
        rev=DEFAULT_REVERSE,
        rows=True,
        cols=True,
        checkerboard=True,
    ):
        # set colors
        self._normal = norm
        self._reverse = rev

        # set features
        self._on: bool = True  # turn all colors on and off
        self._rows: bool = rows  # color rows
        self._cols: bool = cols  # color columns
        self._checkerboard: bool = checkerboard  # do checkerboard?

        # store initial state
        self._row_state: bool = self._rows  # state of rows
        self._col_state: bool = self._cols  # state of columns

    @property
    def row(self):
        self._row_state = not self._row_state
        # if self._checkerboard:
        #     return self.col
        return self

    @property
    def col(self):
        self._col_state = not self._col_state
        return self

    def __str__(self):
        return self._row_state and self._normal or self._reverse


class NpChart:
    def __init__(
        self,
        a: Iterable,
        size: int = 4,
        padding: int = 1,
        pad: str = " ",
        align: NpAlign = NpAlign.left,
    ):

        pass


def np_row(
    a: Iterable,
    size: int = 4,
    padding: int = 1,
    pad: str = " ",
    color: bool = True,
    alt_rows: bool = True,
    alt_columns: bool = True,
    checkerboard: bool = True,
    align: NpAlign = NpAlign.left,
):
    """ Format a row of data for cli output.

        param       description                             default
        ===========================================================
        a -         any iterable data set
        size -      space allowed for each data point       4
        padding -   space between each data point           1
        pad -       character used for padding              ' '
        alt_color - should it alternate colors?             False
        align -     alignment of data in cells              '<'

        """

    ct = ColorToggle() if SUPPORTS_COLOR else ""
    return f'{ct.row}{"".join([f"{ct.col}{x:{align}{size}}{pad*padding}" for x in a])}{ct.reset}'


a = np.arange(5)
arithmetic_lst = ["a", "a + 10", "a - 10", "a * 2", "a / 2", "a // 2"]
for arithmetic in arithmetic_lst:
    evl = eval(arithmetic)
    fmt = np_row(evl, 3, align=NpAlign.right)
    print(f"{arithmetic:>10}: {fmt}")
print()

'''
# print methods of numpy.ndarray without dunders
# print([x for x in dir(evl) if not x.startswith("_")])
