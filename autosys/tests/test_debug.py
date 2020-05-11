#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Tests for Autosys package. For more information:
https://docs.python-guide.org/writing/tests/
"""

# import autosys


def logical_xor(a, b):
    return (a and not b) or (not a and b)


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
