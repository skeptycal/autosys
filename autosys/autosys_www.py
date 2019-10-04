#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
autosys_system.py
"""
from __future__ import absolute_import, print_function

import requests
import autosys
import sys
import os


# import __init__
sys.path.insert(0, os.path.abspath("."))


def url_test(url: str = "http://www.google.com") -> int:
    try:
        r = requests.get(url)
    except (ConnectionError, ConnectionResetError, ConnectionRefusedError, ConnectionAbortedError) as e:
        print(f'Connection error: {e}')
        return 0
    return r.status_code


if __name__ == "__main__":
    print(url_test())
