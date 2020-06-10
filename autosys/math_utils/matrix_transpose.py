#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" # TODO -- @update `AutoSys` package
        copyright (c) 2018 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """
from os import linesep as NL
from typing import Dict, Iterable, List
from dataclasses import dataclass, field, Field, asdict
import json

def roman():
    while True:


@dataclass
class Indent:
    """ Return a foolproof indent string. Indents may include f-strings with
            function output, markdown notation, html tags, css labels, etc.

            To set a static indent string, including f-strings with functions
            or indent_sets, use the form:

            ```
            # general form:
            Indent(ind=f"xxx{func(args)}xxx")

            # example
            def count(n=100):
                for i in range(n):
                    yield i

            ind = Indent(ind=f"#{count()}.")

            ```
            where `func` is the function evaluated elsewhere and `x` is static text portions
            if you wish to use `Indent` to evaluate the function (inlining it),
            use:
            ```
            Indent(ind=f"xxx{eval(func(args))}xxx")



            Return the first successful of these values in this order:
            - first `n` characters in 'c' (0 means *all* of `c`)
            - first `n` chars of `DEFAULT_INDENT_STRING`
            - first `DEFAULT_INDENT_NUMBER` chars of `DEFAULT_INDENT_STRING`
            - the default `DEFAULT_INDENT_STRING`
            - 2 spaces

            This allows useful (and recursive) indents like this:
            ```
            $ xxxx
            xxxx
            - xxxx
            *   xxxx
            I.   xxxx
            a.   xxxx
            1)   xxxx
            f"{_get_next_indent(level=_current_indent_level)}"
            ```
            """

    DEFAULT_INDENT_NUMBER: int = 2
    DEFAULT_INDENT_STRING: str = " " * 12

    n: Field = field(default=DEFAULT_INDENT_NUMBER)
    c: Field = field(default=DEFAULT_INDENT_STRING)
    right_aligned: Field = field(default=False)
    repeat: Field = field(default=False)
    ind: Field = field(default="")
    indent_list: Field = field(default_factory=tuple)

    # flag to ignore `n` and `c` ... eval `ind` directly
    is_eval: Field = field(default=False, init=False)
    has_indent_set: Field = field(default=False, init=False)

    def __post_init__(self):
        """ Setup `self.ind` so that it is ready to return. """
        self._setup_ind()
        self.indent_list = ("I.", "A.", "1.", "a.")

    def _setup_ind(self):
        """ Setup `self.ind` so that it is ready to return. """
        if self.ind:  # ignore `c` and `n`
            self.is_eval = True
        else:
            try:
                self.c = str(self.c)
            except:
                self.c = self.DEFAULT_INDENT_STRING

            try:
                self.n = int(self.n)
            except:
                self.n = self.DEFAULT_INDENT_NUMBER

            if 1 < len(self.c) < 81:  # check `c`
                self.c = self.DEFAULT_INDENT_STRING
            if not (0 < self.n < 81):  # check `n`
                self.n = self.DEFAULT_INDENT_NUMBER

            if self.repeat:  # repeat ignores slicing
                self.ind = self.c * self.n
            elif not self.right_aligned:  # slice left
                self.ind = self.ind[: self.n]
            else:  # slice right
                self.ind = self.ind[-self.n :]

    def __str__(self) -> (str):
        """ Return the current indent string. """
        if self.has_indent_set:
            return self.return_next_indent()
        elif self.is_eval:
            return f"{eval(self.ind)}"
        else:
            try:
                if self.n == 0:
                    return self.c
                else:
                    return self.c[: self.n]
            except:
                try:
                    return DEFAULT_INDENT_STRING[: self.n]
                except:
                    try:
                        return DEFAULT_INDENT_STRING[:DEFAULT_INDENT_NUMBER]
                    except:
                        try:
                            return DEFAULT_INDENT_STRING
                        except:
                            pass
            return "  "


def pretty_list(lst: List, indent="  ") -> (str):
    def _str_gen(x: Iterable, indent=indent):
        return (f"{indent}{str(i)}," for i in x)

    return f"[{NL}{NL.join(_str_gen(lst))}{NL}],"


def pretty_dict(dct: Dict, indent="  "):
    def _str_gen(x: Dict, indent=indent):
        return (f"{indent}{k}: {repr(v)}," for k, v in x.items())

    return f"{{{NL}{NL.join(_str_gen(dct))}{NL}}},"


def transpose_list(lst: List):
    return [list(i) for i in zip(*x)]


x = [[31, 17], [40, 51], [13, 12]]

# ind = Indent(n=2, c="------>", right_aligned=True)

# print(pretty_dict(asdict(ind), indent=f"{ind}"))

# print(x)
# print(transpose_list(x))
print()
# print(pretty_list(x, indent=ind))
print()
# print(pretty_list(transpose_list(x)))

# ind = Indent(n=3, c="->  ")

# for i in range(35, 75):
#     print(f"{ind}{chr(i)}")
def count(n=100):
    for i in range(n):
        yield i


ind = Indent(ind="'#{count(i)}.'")

print(pretty_dict(vars(ind)))

print(ind.__init__)

for i in count(5):
    print(ind)
