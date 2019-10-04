#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Tests for autosys package
"""
import importlib
import os
from pytest import raises
import pytest
import sys
import autosys
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../'))


def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4


# autosys.add_dots('a2345b2345c2345',)
