#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Tests for autosys package
"""
import os
import sys
from pytest import raises
import pytest


def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4
