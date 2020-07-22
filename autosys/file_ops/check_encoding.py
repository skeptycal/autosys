#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def check_encoding(file_name: str = __file__,
                   default: str = "utf-8",
                   verbose: bool = False):
    """ Return encoding specified at the top of file_name.
        If none is specified, return default.

        In other words, find and return this thing:
        ```
        # -*- coding: utf-8 -*-
        ```

        see https://www.python.org/dev/peps/pep-0263/"""
    import re

    pattern = re.compile(rb"[en]?coding[:=\s]+([-\w]*)")

    with open(file_name, mode='rb') as fp:
        lines: bytes = fp.read(300)
    retval = re.findall(pattern, lines)[0].decode("ascii") or default

    if verbose:
        print(f'-- Checking file {file_name}')
        print('-- First few lines')
        print(lines)
        print(f'-- returning encoding match: {retval}')

    return retval


check_encoding(verbose=True)
