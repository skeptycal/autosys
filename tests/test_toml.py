#!/usr/bin/env python3

import unittest

from pathlib import Path

import toml

from typing import Any, Dict, List, Mapping, Sequence

from toml import TomlDecodeError

TOML_DICT_SAMPLE: Dict[str, Any] = {
    'a': 1,
    'b': (1, 2, 3),
    'c': {'a': 'apple', 'b': (4, 5, 6)},
    'd': True,
}

TOML_DICT_SAMPLE_SUBSET: Dict[str, Any] = {'d': True}
TOML_DICT_SAMPLE_SUBSET_ERROR: Dict[str, Any] = {'a': 'apple', 'b': (4, 5, 6)}
TOML_DICT_SAMPLE_SUBSET_FALSE1: Dict[str, Any] = {'a': 'appel', 'b': (4, 5, 6)}
TOML_DICT_SAMPLE_SUBSET_FALSE2: Dict[str, Any] = {'z': 'apple', 'b': (4, 5, 6)}
TOML_DICT_SAMPLE_SUBSET_FALSE3: Dict[str, Any] = {'a': 'appel', 'b': (4, 6, 7)}

encoder = toml.dumps


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
        self.assertTrue(extractDictAFromB(
            TOML_DICT_SAMPLE_SUBSET_ERROR, TOML_DICT_SAMPLE))

    def test_toml_sample_subset_fasle(self):
        # used alternate 'extractDictAFromB'
        # ref: https://stackoverflow.com/a/21213251
        B = TOML_DICT_SAMPLE
        self.assertFalse(extractDictAFromB(TOML_DICT_SAMPLE_SUBSET_FALSE1, B))
        self.assertFalse(extractDictAFromB(TOML_DICT_SAMPLE_SUBSET_FALSE2, B))
        self.assertFalse(extractDictAFromB(TOML_DICT_SAMPLE_SUBSET_FALSE3, B))

    def test_toml_load(self):
        pass

    def test_toml_loads(self):
        pass

    def test_toml_dump(self):
        pass

    def test_toml_dumps(self):
        pass
