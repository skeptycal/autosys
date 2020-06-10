#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" BasicColors - basic ANSI CLI colors

    Part of the `AutoSys` package - utilities for macOS apps
        copyright (c) 2019 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """

try:
    SUPPORTS_COLOR == True
except:
    try:
        from cli import SUPPORTS_COLOR
    except:
        SUPPORTS_COLOR: bool = False

print(SUPPORTS_COLOR)
# some basic CLI colors ..
class BasicColors:
    MAIN: str = "\x1B[38;5;229m" * SUPPORTS_COLOR
    WARN: str = "\x1B[38;5;203m" * SUPPORTS_COLOR
    BLUE: str = "\x1B[38;5;38m" * SUPPORTS_COLOR
    GO: str = "\x1B[38;5;28m" * SUPPORTS_COLOR
    CHERRY: str = "\x1B[38;5;124m" * SUPPORTS_COLOR
    CANARY: str = "\x1B[38;5;226m" * SUPPORTS_COLOR
    ATTN: str = "\x1B[38;5;178m" * SUPPORTS_COLOR
    RAIN: str = "\x1B[38;5;93m" * SUPPORTS_COLOR
    WHITE: str = "\x1B[37m" * SUPPORTS_COLOR
    RESET: str = "\x1B[0m" * SUPPORTS_COLOR
