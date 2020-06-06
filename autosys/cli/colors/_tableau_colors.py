#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Part of the `AutoSys` package - utilities for macOS apps
        copyright (c) 2019 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """

from collections import OrderedDict

# These colors are from Tableau
_TABLEAU_COLORS = (
    ("blue", "#1f77b4"),
    ("orange", "#ff7f0e"),
    ("green", "#2ca02c"),
    ("red", "#d62728"),
    ("purple", "#9467bd"),
    ("brown", "#8c564b"),
    ("pink", "#e377c2"),
    ("gray", "#7f7f7f"),
    ("olive", "#bcbd22"),
    ("cyan", "#17becf"),
)

# Normalize name to "tab:<name>" to avoid name collisions.
TABLEAU_COLORS = OrderedDict(
    ("tab:" + name, value) for name, value in _TABLEAU_COLORS
)
