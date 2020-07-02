#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" # TODO -- @update `AutoSys` package
        copyright (c) 2018 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """

if True:  # * --------------------------------- Imports and Constants
    import re
    from dataclasses import dataclass, Field, field
    from os import linesep as NL
    from typing import Final, List, Tuple
    from string import ascii_uppercase, ascii_lowercase, ascii_letters
    from random import choice

    DEFAULT_RE_FLAGS: Final[int] = re.MULTILINE | re.IGNORECASE
    string = ""


def random_string(stringLength=8):
    letters = ascii_lowercase + ascii_uppercase + " " * 10
    return "".join(choice(letters) for i in range(stringLength))


if True:  # * --------------------------------- ReUtils Class

    @dataclass
    class ReUtils:
        """ Wrapper for common Python3 Regex Utilities. """

        import re

        DEFAULT_RE_FLAGS: Final[int] = re.MULTILINE | re.IGNORECASE
        RE_REPLACE: Final[re.Pattern] = re.compile(pattern=r"[-\s]",
                                                   flags=DEFAULT_RE_FLAGS)

        string = r""

        def sub_it(self,
                   pattern: re.Pattern = RE_REPLACE,
                   repl: str = "_") -> (str, None, Exception):
            """ Return a string where items in `pattern` have been replaced with `repl`. """
            return re.sub(pattern=pattern, repl=repl, string=self.string)

        def re_pip_safe_name(self) -> (str, None, Exception):
            """ Return a name that is converted to pypi safe format.

                Replace ' ' (space) and '-'(hyphen) with _(underscore) using python3 regex
                """
            return RE.sub_it(string=self.string, pattern=RE_REPLACE, repl="_")

        def split_it(self, delimiter: str = "\s") -> (str, None, Exception):
            """ Return a string separated using 'delimiter' using python3 regex. """
            return re.split(pattern=delimiter, string=self.string)

        def dedupe_whitespace(self):
            """ Return a string with duplicate whitespace replaced with ' '. """
            return re.sub(pattern=r"\s+", repl=" ", string=self.string)


if True:  # * --------------------------------- Tests

    test_list1: List[str] = [
        "this is a-test",
        "123_456 789-111",
        "(361) 773-2832",
        ";alskjdfpo82jn sdf83nf ",
    ]
    test_list: List[str] = []

    for i in range(100):
        test_list.append(random_string(25))

    r = ReUtils()
    s: Strang = Strang()
    re_delimiter = r"[\s-]"
    delimiter = r" -"
    print()
    for item in test_list:
        print("---------------------------------")
        print(item)
        print("---------------------------------")
        s = Strang(item)
        print("s:        ", s)
        print("repr:     ", repr(s))
        print("split:    ", s.split_it())
        print("sub:      ", s.sub_it())
        print("upper:    ", s.to_upper_case)
        print("lower:    ", s.to_lower_case)
        print("title:    ", s.to_title_case)
        print("snake:    ", s.to_snake_case)
        print("kebab:    ", s.to_kebab_case)
        print("camel:    ", s.to_camel_case)
        print("pascal:   ", s.to_pascal_case)
