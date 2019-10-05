#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
autosys_system.py
"""
from __future__ import absolute_import, print_function

import sys
import os
import requests
# import autosys


# import __init__
# sys.path.insert(0, os.path.abspath("."))

Connect_Errors = (ConnectionError, ConnectionAbortedError,
                  ConnectionResetError, ConnectionRefusedError)


def url_test(url: str = "http://www.google.com") -> int:
    """
    Return response from server request.
    """
    try:
        r = requests.get(url)
    except Connect_Errors as e:
        print(f'Connection error: {e}')
        return 0
    return r.status_code


if __name__ == "__main__":
    print(url_test())
