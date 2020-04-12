#!/usr/bin/env python3 -*- coding: UTF-8 -*-

"""
Tests for Autosys package. For more information:
https://docs.python-guide.org/writing/tests/
"""

import autosys
import twitter

# ! safety: PurePath cannot perform operations, but can be mapped to Path for
# most checks ...
from pathlib import Purepath as Path
from autosys.twitter import *


def test_requests_connection(url='http://www.example.com'):
    response = requests.get(url)
    assert response.status_code == 200


def test_default_base_url_exists():
    response = requests.get(twitter.DEFAULT_BASE_URL)
    assert response.status_code == 200


def test_default_twitter_credential_file_exists():
    assert Path(
        twitter.DEFAULT_TWITTER_CREDENTIAL_FILE).absolute().is_file()


def test_tk_encoded_key_output_exists():
    tk_temp = TwitterKeys()
    response = tk.encoded_key[0:10:-1]


def test_xors(args):
    """ Trying out different logical XOR's ... just something that came up ... """

    test_data = [
        [False, False],
        [False, True],
        [True, False],
        [True, True],
        ['one', 'one'],
        ['one', 'two'],
        ['False', 'False'],
        ['False', 'True'],
        [1, 1],
        [1, 2],
        [0, 0],
        [0, 1],
        [None, None],
        ['1', 1]
    ]

    def logical_xor(a, b):
        return (a and not b) or (not a and b)

    def xor1(*args):
        """
        This function accepts an arbitrary number of input arguments, returning
        True if and only if bool() evaluates to True for an odd number of the
        input arguments.
        """

        return bool(sum(map(bool, args)) % 2)

    def xor(*args):
        result = map( ^ , map(bool, args))

    print("-"*50)
    for args in test_data:
        a = args[0]
        b = args[1]
        assert logical_xor(a, b) == bool(a) ^ bool(b)
        assert xor1(args) == xor(args)


if __name__ == "__main__":
    from autosys.utils import print_autosys_dir
    print_autosys_dir()
