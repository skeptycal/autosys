# -*- coding: utf-8 -*-

"""
Tests for xxx module
"""

from pytest import raises
import pytest
import sys

_PY2 = sys.version_info[0] == 2


def test_unicode_strings():
    var1 = 2
    var2 = 3
    ans1 = 5
    assert var1 + var2 == ans1
