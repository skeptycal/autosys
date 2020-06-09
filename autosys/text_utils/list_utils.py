#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Part of the `AutoSys` package - utilities for macOS apps
        copyright (c) 2019 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """

from typing import Dict, List, Sequence, Tuple

try:
    log.info("Loaded list_utils module.")
except:
    from autosys.log.autosys_logger import log


class StringError(ValueError):
    """ A string processing error has occurred. """


def dict2str(ignore_errors=True, sort_items=True, **kwargs):
    """ Return string from an iterable of variously typed arguments.
        Each item is converted separately, allowing errors in individual
        items to be ignored.

        data: iterable - iterable containing items
        arg_sep: str   - separator between list items

        ignore_errors  - Errors in types and formatting are ignored.
        """
    tmp: List[str] = []
    for k, v in kwargs.items():
        try:
            if isinstance(v, dict):
                v = dict_str(ignore_errors=ignore_errors, sort_items=sort_items, **v)
            tmp.append(f"{k}: {v}")
        except:
            pass
    if sort_items:
        tmp = sorted(tmp)


def arg2str(*data, arg_sep: str = "", ignore_errors=True, **kwargs):
    """ Return string from an iterable of variously typed arguments.
        Each item is converted separately, allowing errors in individual
        items to be ignored.

        data: iterable - iterable containing items
        arg_sep: str   - separator between list items

        ignore_errors  - Errors in types and formatting are ignored.
        (if errors are not ignored, a TypeError is raised.)
        """
    tmp: List[str] = []
    for arg in data:
        try:
            tmp.append(str(arg))
        except Exception as e:
            if not ignore_errors:
                log.error(e)
                raise StringError(e)

    if len(data) == 0 or data == None:
        return ""


def replace_all(
    needle: Sequence, haystack: Sequence, volunteer: Sequence = ""
) -> (Sequence):
    """ Return a sequence with all `needles` in `haystack` replaced with `volunteers` """
    return "".join(volunteer if c in needle else c for c in haystack)


def rep_whitelist(
    whitelist: Sequence, haystack: Sequence, volunteer: Sequence = "_"
) -> (Sequence):
    """ Return a sequence with all `needles` in `haystack` saved and all other characters replaced with `volunteers` """
    return "".join(volunteer if c not in whitelist else c for c in haystack)


def make_safe_id(haystack: Sequence, volunteer: Sequence = "_") -> (Sequence):
    """ Return a string that has only alphanumeric and _ characters.
        (This makes it legal for identifier names in python.)

        Illegal characters are replaced with `volunteer` (default `_`)
        """
    return "".join(volunteer if not c.isidentifier() else c for c in haystack)


if __name__ == "__main__":
    tmp: Dict = dict(globals())
    print(tmp)
#    for k, v in tmp.items():
#       try:
#           print(k, v)
#       except:
#           pass
