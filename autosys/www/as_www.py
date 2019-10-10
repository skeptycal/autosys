#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" as_www.py """
# copyright (c) 2019 Michael Treanor
# https://www.github.com/skeptycal
# https://www.twitter.com/skeptycal
# from __future__ import absolute_import, print_function

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

    print()
    urls = ['http://www.google.com', 'https://www.google.com',
            'https://www.twitter.com/skeptycal']
    # 'https://www.skeptycal.com'
    for url in urls:
        res = url_test(url)
        print()
        if res == 200:
            print(f'Successful connection to {url} ...response: {res}')
        else:
            print(f'No connection to {url} ... response: {res}')
