#!/usr/bin/env python3
""" A few simple tests used to check pytest, unittest, and coverage configuration. """
import unittest

from pathlib import Path
from typing import Any, List, Mapping, Sequence

sample_true_test_values: List[Any] = [
    2,
    2.3,
    'yes',
    '1',
    '1.7',
    __file__,
    object(),
    True,
    (3 > 2),
    {'a': '1'},
    [None],
    [[]]
]

sample_false_test_values: List[Any] = [
    0,
    0.0,
    None,
    '',
    "",
    [],
    {},
    (),
    (2 > 3),
    dict(),
    (None),
    (())
]

pseudo_true: List[str] = ["1", "true", "yes", "y", "ok", "on"]
pseudo_false: List[str] = ["0", "false", "no", "n", "nok", "off"]


def add(x: int, y: int) -> (int):
    return x + y


def multiply(x: int, y: int) -> int:
    return x * y


def bool_check(key) -> bool:

    if isinstance(key, Path):
        return key.exists()
    if isinstance(key, bool):
        return key
    if isinstance(key, (int, float, complex)):
        return key != 0
    if isinstance(key, (Mapping, Sequence)):
        return len(key) > 0
    if isinstance(key, bytes):
        key = key.decode()
    key = key.lower()
    return int(key) != 0


def pseudo_bool(key) -> bool:
    """
    Return True/False for common string representations of 'yes/no'
    """
    try:
        key = str(key).lower()
        return key in pseudo_true or not (key in pseudo_false)
    except:
        return None


class BasicTests(unittest.TestCase):

    def test_add(self):
        """
        Test addition of 100 pairs of ints.
        """
        for i in range(100):
            test_x = 3 * i
            test_y = 4 * i
            assert test_x + test_y == add(test_x, test_y)
            self.assertEqual(
                add(test_x, test_y),
                test_x + test_y,
                f"Should be {test_x + test_y}")

    def test_multiply(self):
        """
        Test multiplication of 100 pairs of ints.
        """
        for i in range(100):
            test_x = 3 * i
            test_y = 4 * i
            assert test_x * test_y == multiply(test_x, test_y)
            self.assertEqual(
                multiply(test_x, test_y),
                test_x * test_y,
                f"Should be {test_x * test_y}")

    def test_true(self):
        """
        Test True
        """
        self.assertTrue(True, "Should be True.")
        assert True

    def test_false(self):
        """
        Test False
        """
        self.assertFalse(False, "Should be False.")
        assert bool(0) == False

    def test_bools(self):
        """
        Test various forms of 'True' and 'False' equivalent values.
        """

        for value in sample_false_test_values:
            self.assertFalse(bool(value), f"bool({value}) should be False.")
            assert bool(value) == False

        for value in sample_true_test_values:
            self.assertTrue(bool(value), f"bool({value}) should be True.")
            assert bool(value) == True

    def test_pseudobools(self):
        for value in pseudo_false:
            self.assertFalse(pseudo_bool(value),
                             f"pseudo_bool({value}) should be False.")
            assert pseudo_bool(value) == False

        for value in pseudo_true:
            self.assertTrue(pseudo_bool(value),
                            f"pseudo_bool({value}) should be True.")
            assert pseudo_bool(value) == True
