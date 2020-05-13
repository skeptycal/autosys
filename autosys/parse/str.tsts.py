#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2020 Michael Treanor
# License: MIT (http://www.opensource.org/licenses/mit-license.php)
"""
testing some things with strings and fstrings ... with wings

https://www.python.org/dev/peps/pep-0498/

fstring definition:
    ```
    f ' <text> { <expression> <optional !s, !r, or !a> <optional : format specifier> } <text> ... '
    ```
"""


class NewStr(str):
    pass