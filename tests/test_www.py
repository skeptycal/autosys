#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_www.py
"""
# copyright (c) 2019 Michael Treanor
# https://www.github.com/skeptycal
# https://www.twitter.com/skeptycal

from __future__ import absolute_import, print_function
import pytest
from pytest import raises
from autosys.as_www import url_test


def test_url_test():
    urls = ['http://www.google.com', 'https://www.google.com',
            'https://www.twitter.com/skeptycal', 'http://192.168.0.1']
    # 'https://www.skeptycal.com'
    for url in urls:
        assert url_test(url) == 200
