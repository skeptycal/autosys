#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
autosys_system.py
"""
from __future__ import absolute_import, print_function
import pytest
from pytest import raises
from autosys.as_www import url_test


def test_url_test():
    assert url_test() == 200


def test_url():
    assert url_test('192.168.0.1') == 200
