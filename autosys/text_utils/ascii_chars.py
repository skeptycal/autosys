#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from typing import Dict, List
from os import linesep as NL
from dataclasses import dataclass


class Ascii_Chars(dict):
    def __init__(self, indent=2):
        self.indent: int = indent
        self.ascii_range: List[int] = range(0, 255)
        self.indent_char = " " * self.indent
        self = {f"c{x}": chr(x) for x in self.ascii_range}

    def pprint(self, indent: int = 2) -> str:
        return NL.join([f"{' '* indent}{k:>5.5}: {v:<2.2}" for k, v in self.items()])


print(Ascii_Chars())
a = Ascii_Chars()
print(a.ascii_range)

# print(NL.join([f"{' '* indent}{k}: {v}" for k, v in ascii_chars.items()]))
