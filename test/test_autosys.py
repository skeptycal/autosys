#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Tests for autosys package
"""
import importlib
import os
import sys
from pytest import raises
import pytest
# import autosys_system


# sys.path.insert(0, os.path.abspath("."))
# sys.path.insert(0, os.path.abspath("../"))
# syspy = importlib.import_module("sys-py")


def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4


# _PY2 = sys.version_info[0] == 2
