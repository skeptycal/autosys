#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Initial Basic Tests for Autosys package.
For more information: https://docs.python-guide.org/writing/tests/
"""


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5
