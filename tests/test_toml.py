#!/usr/bin/env python3

from dataclasses import dataclass
import unittest

from pathlib import Path

import toml

from typing import Any, Dict, List, Mapping, MutableMapping, Sequence, Tuple

from toml import TomlDecodeError

TOML_DICT_SAMPLE: Dict[str, Any] = {
    'a': 1,
    'b': (1, 2, 3),
    'c': {'a': 'apple', 'b': (4, 5, 6)},
    'd': True,
}

TOML_DICT_SAMPLE: Dict[str, Any] = {'a': 'apple', 'b': (4, 5, 6)}

TOML_DICT_SAMPLES: List[Tuple[Dict[str, Any], bool]] = [
    ({'d': True}, True),
    ({'a': 1}, True),
    ({'a': 'apple'}, True),
    ({'c': {'a': 'apple', 'b': (4, 5, 6)}}, True),
    ({'d': False}, False),
    ({'a': 'apple', 'b': (4, 5, 6)}, True),
    ({'a': 'appel', 'b': (4, 5, 6)}, False),
    ({'z': 'apple', 'b': (4, 5, 6)}, False),
    ({'a': 'appel', 'b': (4, 6, 7)}, False),
]


@ dataclass
class BooleanTest:
    """ A data type that holds a name, boolean outcome, and dictionary value. """
    _name: str
    _flag: bool
    _value: MutableMapping[str, Any]


TOML_DICT_SAMPLES: List[BooleanTest] = [
    BooleanTest('', True, {'d': True}),
    BooleanTest('', True, {'a': 1}),
    BooleanTest('', True, {'a': 'apple'}),
    BooleanTest('', True, {'c': {'a': 'apple', 'b': (4, 5, 6)}}),
    BooleanTest('', False, {'d': False}),
    BooleanTest('', True, {'a': 'apple', 'b': (4, 5, 6)}),
    BooleanTest('', False, {'a': 'appel', 'b': (4, 5, 6)}),
    BooleanTest('', False, {'z': 'apple', 'b': (4, 5, 6)}),
    BooleanTest('', False, {'a': 'appel', 'b': (4, 6, 7)}),
]


def gen_toml_test_samples():
    for x in TOML_DICT_SAMPLES:
        for d, b in x:
            yield (d, b)


class BooleanDict:
    data = TOML_DICT_SAMPLES

    def __init__(self, flag: bool) -> None:

        self.flag = flag


def extractDictAFromB(A: Dict[str, Any], B: Dict[str, Any]) -> Dict[str, Any]:
    # updated to recursive to allow for dict values assigned to keys
    retval: Dict[str, Any] = {}
    for k, v in A.items():
        if isinstance(v, dict):
            retval.update(extractDictAFromB(A=v, B=B))
        elif k in B.keys():
            if A[k] == B[k]:
                retval[k] = v
    return retval


def dict_is_subset(dict1, dict2):
    return dict1.items() <= dict2.items()


class TomlTest(unittest.TestCase):
    def test_toml_sample_structure(self):
        self.assertIsInstance(TOML_DICT_SAMPLE, dict)
        self.assertIsInstance(TOML_DICT_SAMPLE_SUBSET, dict)
        self.assertIsInstance(TOML_DICT_SAMPLE_SUBSET_ERROR, dict)

    def test_toml_sample_subset(self):
        self.assertDictContainsSubset({'d': True},
                                      TOML_DICT_SAMPLE_SUBSET)
        self.assertDictContainsSubset(
            TOML_DICT_SAMPLE_SUBSET, TOML_DICT_SAMPLE)

    def test_toml_sample_subset_duplicate(self):
        # this causes an error due to duplicate keys in dict and subset
        # self.assertDictContainsSubset(
        #     TOML_DICT_SAMPLE_SUBSET_ERROR, TOML_DICT_SAMPLE)
        # (and assertDictContainsSubset is deprecated ...)
        # used alternate 'extractDictAFromB'
        # ref: https://stackoverflow.com/a/21213251
        self.assertTrue(extractDictAFromB(TOML_DICT_SAMPLE,
                                          TOML_DICT_SAMPLE_SUBSET_ERROR))

    def test_toml_sample_subset_fasle(self):
        # used alternate 'extractDictAFromB'
        # ref: https://stackoverflow.com/a/21213251
        B = TOML_DICT_SAMPLE
        self.assertFalse(extractDictAFromB(TOML_DICT_SAMPLE_SUBSET_FALSE1, B))
        self.assertFalse(extractDictAFromB(TOML_DICT_SAMPLE_SUBSET_FALSE2, B))
        self.assertFalse(extractDictAFromB(TOML_DICT_SAMPLE_SUBSET_FALSE3, B))

    def test_toml_sample_subset_with_operator(self):
        dict1 = TOML_DICT_SAMPLE
        for d, b in gen_toml_test_samples():

            self.assertTrue(dict_is_subset(TOML_DICT_SAMPLE_SUBSET, dict1))
            self.assertTrue(dict_is_subset(d, dict1))

    def test_toml_load(self):
        pass

    def test_toml_loads(self):
        pass

    def test_toml_dump(self):
        pass

    def test_toml_dumps(self):
        pass
