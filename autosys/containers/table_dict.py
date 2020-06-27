#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" table_dict

    print a pretty table from a dictionary

    ---
    Part of the [AutoSys][1] package

    Copyright (c) 2018 [Michael Treanor][2]

    AutoSys is licensed under the [MIT License][3]

    [1]: https://www.github.com/skeptycal/autosys
    [2]: https://www.twitter.com/skeptycal
    [3]: https://opensource.org/licenses/MIT
    """

from typing import Dict


def table_dict(_vars: Dict, width=60, divider=": ", indent=2, key_size=15):
    min_width: int = key_size
    print("-" * width)
    key_size = ((key_size := width // 4) < min_width) or min_width
    print(key_size)
    value_size = width - key_size - indent - len(divider) - 1
    for k, v in _vars.items():
        val = str(v)[:value_size]
        print(f"{indent*' '}{k:<{key_size}.{key_size}}{divider}{val}")
