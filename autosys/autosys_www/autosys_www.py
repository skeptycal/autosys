#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
autosys_system.py
"""
from __future__ import absolute_import, print_function

import requests
import sys
import os


# import __init__
sys.path.insert(0, os.path.abspath("."))


def _url_test(
    url: str = "http://www.google.com") -> int: return requests.get(url)


if __name__ == "__main__":
    print(_url_test())
