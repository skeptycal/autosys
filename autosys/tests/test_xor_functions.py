#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Tests for Autosys package. For more information:
https://docs.python-guide.org/writing/tests/
"""

# import autosys
# from autosys.twitter import twitter
# from autosys.twitter.twitter import *

# ! safety: PurePath cannot perform operations,
#   but can be mapped to Path for most tests ...
# from pathlib import PurePath as Path


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
    # args = map(bool, args1)
    result = bool(args[0])
    for arg in args[1:]:
        result = result ^ bool(arg)


def xor_np(x, y):
    try:
        return np.abs(x-y)
    except Exception as e:
        raise Exception("NP abs function error.{NL}{e}")


def test_xors():
    """ Trying out different logical XOR's ... just something that came up ... """

    test_data = [
        [False, False, ],
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

    args = test_data

    # print("-"*50)
    # for args in test_data:
    #     a = args[0]
    #     b = args[1]
    #     assert logical_xor(a, b) == bool(a) ^ bool(b)
    #     assert xor1(args) == xor(args)
