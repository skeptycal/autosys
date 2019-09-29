#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""
Tests for autosys package
"""
import importlib
import os
from pytest import raises
import pytest
import sys
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../'))

autosys = importlib.import_module("autosys")

_PY2 = sys.version_info[0] == 2


def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4
