#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pysystem.py - System utilities for Python on macOS
"""

# the sys.path starts with the directory containing pysys.py which we want to remove as
# that dir might be anywhere and could contain anything; it's not needed for locating
# the pysys modules since those will be in site-packages once pysys is installed
from __future__ import absolute_import, print_function

import inspect
import locale
import logging
import os
import sys
import time
import traceback
from typing import Any, Dict, List

from version import __version__

script_path = os.path.abspath(sys.path[0])
sys.path = [p for p in sys.path if os.path.abspath(p) != script_path]

sys.path.insert(0, os.path.abspath("."))  # insert pwd

##############################################
locale.setlocale(locale.LC_ALL, "")
CODE = locale.getpreferredencoding()


if __name__ == "__main__":
    pass
    # log = logging.getLogger()
    # print(_run_tests())
    # print()
    # print("... Tests Complete.")
    # _pprint_dict_table

    # Parts of the setup and skeleton of pysystem were inspired by:
    # PySys System Test Framework, Copyright (C) 2006-2019 M.B. Grieve

    # This library is free software; you can redistribute it and/or
    # modify it under the terms of the GNU Lesser General Public
    # License as published by the Free Software Foundation; either
    # version 2.1 of the License, or (at your option) any later version.

    # This library is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    # Lesser General Public License for more details.

    # You should have received a copy of the GNU Lesser General Public
    # License along with this library; if not, write to the Free Software
    # Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
