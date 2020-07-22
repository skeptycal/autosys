#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" dis_block.py """
# copyright (c) 2019 Michael Treanor
# https://www.github.com/skeptycal
# https://www.twitter.com/skeptycal


if True:  # imports
    import dis
    import sys
    from pathlib import Path
    from collections import Counter, deque
    from time import perf_counter_ns as timer
    from typing import Deque, Dict, List

    try:
        import ujson as json
    except ImportError:
        import json
if True:  # constants

    _PY2: bool = sys.version_info[0] == 2

    class CB_Options:
        """ Initialization option choices for CodeBlock objects. """

        ON_DEMAND = 0  # minimal - only processed as needed (jit)
        ON_INIT = 1  # basic - only generated on object creation (precompiled)
        ON_ALL = 2  # thorough - processed when created and refreshed on demand

    CB_OPTIONS_DEFAULT: CB_Options = CB_Options.ON_DEMAND


class CodeBlock:
    _code: str
    _dis: str
    _name: str
    _result: str

    def __init__(self, name: str, s: str = "", options=CB_Options.ON_DEMAND):
        self.name = name
        self.code = self.name if s == "" else s

    @property
    def dis(self):
        return dis.dis(self.code)

    @property
    def result(self):
        return eval(self.code)

    @property
    def compile(self):
        return compile(self.code)

    def __str__(self):
        return self.name


class TestRun:
    trials: int = 1
    repeats: int = 100
    avgtime: Deque


class CodeBlocks:
    """ Collection of CodeBlock objects with test run instructions.
        Used to load and setup CodeBlock objects before profiling runs.
        """

    __data = {}
    __cb_list: List = []
    _file = ""
    _options: CB_Options

    def __init__(self, file=None, opt: CB_Options = CB_OPTIONS_DEFAULT):
        super().__init__()
        self._options = opt
        if Path(file).exists():
            self._file = file

    @property
    def options(self):
        return self._options

    def load_dict(self, d: Dict):
        """ Load data from dict. """
        for n, k, v in enumerate(d):
            self.cb_list.append(CodeBlock(k, v, self.options))
            pass
        self.data = d

    def save_json(self, f):
        """ Save data to json file. """
        pass

    def print(self):
        for cb in cb_list:
            print(cb)


code_tests = {"_PY2": "", "sys.argv": ""}

# print(A)
# print(A.result)

# print(f"disassemble test A: {dis_test_A}")
# print(f"result of A = {dis_test_A()}")
# print(dis.dis(dis_test_A))

# print(f"disassemble test B: {dis_test_B}")
# print(f"result of B = {dis_test_B()}")
# print(dis.dis(dis_test_B))
