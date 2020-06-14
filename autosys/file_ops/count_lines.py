#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Count Lines
    ---
    count_lines - count the number of lines in a text file

    AutoSys
    ---
    Part of the [AutoSys][1] package

    Copyright (c) 2018 [Michael Treanor][2]

    AutoSys is licensed under the [MIT License][3]

    [1]: https://www.github.com/skeptycal/autosys
    [2]: https://www.twitter.com/skeptycal
    [3]: https://opensource.org/licenses/MIT
    """

# 'Standard Library'
from os import argv
from pathlib import Path

# 'package imports'
from autosys.file_ops import codec_open

# (venv) ➜  autosys (dev) ✗)python3 -c "import sys; print(f'{sys.argv}'); n=0; with open(sys.argv[1]): n += 1; print(n);" 'pip list'
