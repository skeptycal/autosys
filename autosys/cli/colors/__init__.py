#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Part of the `AutoSys` package - utilities for macOS apps
        copyright (c) 2019 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """
from ._css4 import CSS4_COLORS
from ._matplotlib import BASE_COLORS
from ._tableau_colors import TABLEAU_COLORS
from ._xkcd_colors import XKCD_COLORS

__all__ = [
    'CSS4_COLORS',
    'BASE_COLORS',
    'TABLEAU_COLORS',
    'XKCD_COLORS',
]
