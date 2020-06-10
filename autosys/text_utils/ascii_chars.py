#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import text_utils
from text_utils import *
from pprint import pformat

@dataclass
class Ascii_Chars(dict):
    indent: int = 2
    ascii_range: List[int] = range(0, 255)
    indent_char: str = " "

    def __post_init__(self, indent=2):
        self.ind: str = self.indent_char * self.indent
        self.update({f"c{x}": chr(x) for x in self.ascii_range if chr(x)})

    def __str__(self, indent: int = 2) -> (str):
        return pformat(self.items(),indent=self.indent, depth=5)
        return ", ".join(
        [f"{self.ind}{x}" for x in self.to_list()]
    )

    #? ------------------------ contents checks

    def is_printable(self, value):
        return str(value).isprintable

    def is_alpha(self, value):
        return str(value).isalpha

    def is_alphanum(self, value):
        return str(value).isalnum

    def is_hex(self, value):
        return value in STR_HEX

    def is_name(self, value):
        return str(value).isidentifier

    def is_punc(self, value):
        return value in STR_PUNCTUATION

    def is_white(self, value):
        return str(value).isspace

    def is_ascii(self, value):
        return str(value).isascii

    def is_dec(self, value):
        return str(value).isdecimal

    def is_digit(self, value):
        return str(value).isdigit

    def is_lower(self, value):
        return str(value).islower

    def is_upper(self, value):
        return str(value).isupper

    def is_title(self, value):
        return str(value).istitle

    #? ------------------------ conversions

    def to_hex(self,value):
        return f"{value:x}"

    def to_octal(self,value):
        return f"{value:o}"

    def to_sci(self,value):
        return f"{value:e}"

    def to_title(self,value):
        return str(value).title

    #? ------------------------ type conversions

    def to_list(self):
        # return self.values()
        return [f"{k}: {v}" for k, v in self.items() if self.is_printable(v)]

    #? ------------------------ formatting

    def to_columns(self, n: int = 3, width: int = 80):
        items = self.to_list()
        print(items)
        size: int = len(items)
        print(size)
        size_per: int = size // n
        print(size_per)
        result = []
        for i, x in enumerate(items):

            result = NL.join([f"{x:>15.15}     |     {x:>15.15}" for x in items])
        print(result)


print(Ascii_Chars())

a = Ascii_Chars()
print(repr(a))
print(str(a))
# a.to_columns()
