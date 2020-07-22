#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" re_bool.py """
# copyright (c) 2020 Michael Treanor
# https://www.github.com/skeptycal
# https://www.twitter.com/skeptycal


class ReBool(int):
    def __new__(cls, value):
        return int.__new__(cls, bool(value))

    def __repr__(self):
        return "MyBool." + ["False", "True"][self]

    def __str__(self):
        return f"bool{self}"


x = ReBool(1)
print(x)
print(ReBool(2) == 1)
print(ReBool(1) == 1)
print(ReBool(2) == 2)
print(ReBool(2))
