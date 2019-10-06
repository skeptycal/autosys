#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" test_as_testing.py """
# copyright (c) 2019 Michael Treanor
# https://www.github.com/skeptycal
# https://www.twitter.com/skeptycal

# from __future__ import absolute_import, print_function
import pytest
from pytest import raises
from autosys.as_testing import *


def test_v_name():
    i = 25
    j = 3.14
    s = 'Newport News'
    t = 'fsadf$f%dj!d/fasd//'
    l = [1, 2, '3']
    d = dict(globals())
    assert v_name(i) == 'i'
    assert v_name(j) == 'j'
    assert v_name(s) == 's'
    assert v_name(t) == 't'
    assert v_name(l) == 'l'
    assert v_name(d) == 'd'
