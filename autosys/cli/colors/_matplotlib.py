#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Part of the `AutoSys` package - utilities for macOS apps
        copyright (c) 2019 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """

# These color mappings were taken from matplotlib
# https://github.com/matplotlib/matplotlib/blob/master/lib/matplotlib/_color_data.py
# matplotlib license:
#   https://matplotlib.org/users/license.html
# the matplotlib license is a BSD and GPL compatible license based on the PSF license:

# PSF license:
#   https://docs.python.org/3/license.html

# Note: GPL-compatible doesn’t mean that we’re distributing Python under the
# GPL. All Python licenses, unlike the GPL, let you distribute a modified
# version without making your changes open source. The GPL-compatible licenses
# make it possible to combine Python with other software that is released
# under the GPL; the others don’t.

# matplotlib 'single letter colors' called BASE_COLORS
BASE_COLORS = {
    "b": (0, 0, 1),  # blue
    "g": (0, 0.5, 0),  # green
    "r": (1, 0, 0),  # red
    "c": (0, 0.75, 0.75),  # cyan
    "m": (0.75, 0, 0.75),  # magenta
    "y": (0.75, 0.75, 0),  # yellow
    "k": (0, 0, 0),  # black
    "w": (1, 1, 1),  # white
}
