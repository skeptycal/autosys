# -*- coding: utf-8 -*-

"""
Tests for sys-py module
"""
import importlib
import os
import sys

import pytest
from pytest import raises

sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath("../"))

syspy = importlib.import_module("sys-py")

_PY2 = sys.version_info[0] == 2


def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4
