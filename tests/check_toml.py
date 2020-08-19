#!/usr/bin/env python3

from dataclasses import dataclass, astuple, asdict
from os import linesep as NL
from pprint import pformat
import unittest
from loguru import logger

from pathlib import Path
import toml

from typing import Any, Dict, Generator, List, Mapping, MutableMapping, NamedTuple, Sequence, Tuple

from toml import TomlDecodeError

logger.debug('logging ...')

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


class One:
    def __init__(self, klass):
        self.klass = klass
        self.instance = None

    def __call__(self, *args, **kwds):
        if self.instance == None:
            self.instance = self.klass(*args, **kwds)
        return self.instance


@logger.catch()
@ dataclass
class BooleanTest:
    """ A data type that holds a name, boolean outcome, and dictionary value. """
    name: str
    flag: bool
    value: MutableMapping[str, Any]

    def __post_init__(self):
        pass

    def to_tuple(self):
        return astuple(self)

    def __iter__(self) -> Tuple[str, bool, MutableMapping]:
        yield (self.name, self.flag, self.value)

    # def __str__(self) -> str:
    #     # return pformat(self)
    #     return f"{self.name:<20.20}  assert{str(self.flag):<5.5}  => {self.value}"


@One
class BooleanTestSet(list):
    max_length: int = 0
    __instance = None

    def __init__(self, b) -> None:
        print(id(self))

    # def __new__(cls, val):
    #     if BooleanTestSet.__instance is None:
    #         BooleanTestSet.__instance = list.__new__(cls)
    #     BooleanTestSet.__instance.val = val
    #     return BooleanTestSet.__instance

    # def gen(self) -> Generator[BooleanTest]:
    #     i: BooleanTest = None
    #     for i in self:
    #         yield i

    # def items(self) -> Generator[Tuple[str, str, str]]:
    #     # for _ in self.gen():
    #     yield ((_.name, _.flag, _.value) for _ in self.gen())

    # def text_width(self) -> Tuple[str]:
    #     for t in self.items():
    #         return n, f, v

    def __str__(self):
        return pformat(self)
        # return NL.join(str(_) for _ in self)


b = BooleanTestSet([
    BooleanTest('boolean value', True, {'d': True}),
    BooleanTest('dictionary value', True, {'a': 1}),
    BooleanTest('subdict value', True, {'a': 'apple'}),
    BooleanTest('complex value', True, {'c': {'a': 'apple', 'b': (4, 5, 6)}}),
    BooleanTest('boolean false', False, {'d': False}),
    BooleanTest('dict with tuple', True, {'a': 'apple', 'b': (4, 5, 6)}),
    BooleanTest('dict bad value', False, {'a': 'appel', 'b': (4, 5, 6)}),
    BooleanTest('dict bad key', False, {'z': 'apple', 'b': (4, 5, 6)}),
    BooleanTest('dict bad tuple', False, {'a': 'apple', 'b': (4, 6, 7)}),
])

# TOML_DICT_SAMPLES: List[Tuple[Dict[str, Any], bool]] = [

for x in TOML_DICT_SAMPLES:
    for t in x:
        for d, b in t:
            print(d, b)
        # print(t)

print(b)
# print(vars(b))
# print()
# print(id(b))
# for item in b.gen():
# print(f"Test '{item.name:<15}' should be {item.flag}.")

# print(b[0].to_tuple())

# print(b.text_width())
# for n, f, v in b.items():
#     print(n, f, v)


class Borg:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class Singleton(Borg):
    def __init__(self, arg):
        Borg.__init__(self)
        self.val = arg

    def __str__(self): return self.val


# Singleton/ClassVariableSingleton.py
class BooleanTestSet(object):
    __instance = None

    def __new__(cls, val):
        if BooleanTestSet.__instance is None:
            BooleanTestSet.__instance = object.__new__(cls)
        BooleanTestSet.__instance.val = val
        return BooleanTestSet.__instance
