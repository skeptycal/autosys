#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sys import version_info

PY_MAJOR: int = version_info.major
PY_MINOR: int = version_info.minor

try:
    assert version_info > (3, 5)

    def merge_two_dicts(x, y):
        print('new_version')
        return {**x, **y}

except AssertionError:
    def merge_two_dicts(x, y):
        """Given two dictionaries, merge them into a new dict as a shallow copy."""
        print('old_version')
        z = x.copy()
        z.update(y)
        return z


def merge_dicts(*dict_args):
    """
    Given any number of dictionaries, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dictionaries.
    """
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result


x = dict(a=1, b=2, c=3)
y = dict(d=4, e=5, f=6)

print(merge_two_dicts(x, y))

'''
old_version
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
new_version
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

'''
