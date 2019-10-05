#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
autosys_system.py
"""
from __future__ import absolute_import, print_function

import sys
import os
import requests


CONNECT_ERRORS = (ConnectionError, ConnectionAbortedError,
                  ConnectionResetError, ConnectionRefusedError)


def url_test(url: str = "http://www.google.com") -> int:
    """
    Return response from server request.
    """
    try:
        r = requests.get(url)
    except CONNECT_ERRORS as e:
        print(f'Connection error: {e}')
        return 0
    return r.status_code


if __name__ == "__main__":
    print(url_test())
