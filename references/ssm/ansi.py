#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# Copyright (c) 2019 Michael Treanor
# MIT <https://opensource.org/licenses/MIT>
# Michael Treanor  <skeptycal@gmail.com>
# https://www.github.com/skeptycal
# Intended for Python 3.7+ , ymmv on others
# ============================================================================

import os
from pygments import highlight
from pygments.style import Style
from pygments.token import Token
from pygments.lexers import Python3Lexer
from pygments.formatters import Terminal256Formatter


class MyStyle(Style):
    styles = {
        # Token.String:     'ansibrightblue bg:ansibrightred',
        Token.String: 'ansiyellow bg:ansibrightblack',
    }


def pyg(code: str, style: Style = MyStyle) -> str:
    return highlight(code, Python3Lexer(), Terminal256Formatter(style=style))


# from .csscolors import parse_rgb, css_colors
# * ######################## ANSI constants for common colors
if True:
    MAIN = '\001\033[38;5;229m'
    WARN = '\001\033[38;5;203m'
    COOL = '\001\033[38;5;38m'
    BLUE = '\001\033[38;5;38m'
    GO = '\001\033[38;5;28m'
    CHERRY = '\001\033[38;5;124m'
    CANARY = '\001\033[38;5;226m'
    ATTN = '\001\033[38;5;178m'
    PURPLE = '\001\033[38;5;93m'
    RAIN = '\001\033[38;5;93m'
    WHITE = '\001\033[37m'
    RESTORE = '\001\033[0m\002'
    RESET_FG = '\001\033[0m'

    # * ######################## functions for printing lines in common colors
    def br():
        print()
        #  { print "\n"; } # yes, this is a fake cli version of <br />

    def ce(*args, **kwargs):
        print(args, kwargs, RESET_FG)

    def cprint(color, *args, **kwargs):
        pass

    def me(*args, **kwargs):
        print(MAIN, args, kwargs, RESET_FG)

    def warn(*args, **kwargs):
        print(WARN, args, kwargs, RESET_FG)

    def blue(*args, **kwargs):
        print(COOL, args, kwargs, RESET_FG)

    def green(*args, **kwargs):
        print(GO, args, kwargs, RESET_FG)

    def cherry(*args, **kwargs):
        print(CHERRY, args, kwargs, RESET_FG)

    def canary(*args, **kwargs):
        print(CANARY, args, kwargs, RESET_FG)

    def attn(*args, **kwargs):
        print(ATTN, args, kwargs, RESET_FG)

    def purple(*args, **kwargs):
        print(PURPLE, args, kwargs, RESET_FG)

    def rain(*args, **kwargs):
        print(RAIN, args, kwargs, RESET_FG)

    def white(*args, **kwargs):
        print(WHITE, args, kwargs, RESET_FG)

if __name__ == "__main__":
    base: str = "Hello World from {}".format(os.path.basename(__file__))
    code: str = 'print("' + base + '")'
    result = highlight(code, Python3Lexer(),
                       Terminal256Formatter(style=MyStyle))
    print(result.encode())
    print(result)

    code = 'print("Hello World")'
    result = highlight(code, Python3Lexer(),
                       Terminal256Formatter(style=MyStyle))
    # result = pyg(code, style)
    print(result.encode())
    print(result)
