#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" as_80col.py - cli utility with string and color functions. """
# copyright (c) 2019 Michael Treanor
# https://www.github.com/skeptycal
# https://www.twitter.com/skeptycal

# 'Standard Library'
import os
import textwrap

# 'package imports'
from autosys.as_constants import PY_ENV
# import autosys.as_constants
from autosys.as_system import py_shell
from autosys.colors import COLORS, STYLES, color

# sys.path.insert(0, os.path.abspath("."))

# Turn off color when using ipython, otherwise leave it on
ENABLE_COLOR: bool = True
if py_shell() in ["ipython", "ipython-notebook"]:
    ENABLE_COLOR = False


def test_styles(bg, fg):
    for style in (None,) + STYLES:
        cname = fg or "default"
        # renamed None color to default to avoid confusion wiht normal style
        if cname.startswith("bright"):
            cname = cname[6:].upper()
        text = cname[:5].ljust(6)
        print(color(text, fg=fg, bg=bg, style=style), end=" ")
    print()


# doubled number of colors, so have to split test into halves to
# test on standard 80-column terminal

colors = [None] + list(COLORS[:8])
brights = list(COLORS[8:])

for bg in colors:
    for fg in colors:
        test_styles(bg, fg)
    for fg in brights:
        test_styles(bg, fg)
for bg in brights:
    for fg in colors:
        test_styles(bg, fg)
    for fg in brights:
        test_styles(bg, fg)

for i in range(256):
    if i % 64 == 0:
        print()
    print(color(" ", bg=i), end="")

print()
