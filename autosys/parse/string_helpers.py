#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Sequence

# from sys import stdout
# from os import linesep as NL, environ as ENV
# from platform import platform
# from io import TextIOWrapper
# from dataclasses import dataclass

# TODO profile and compare with RE and C functions

def isutf8(f):
    # TODO - create a function version of `isutf8 -li *`
    pass

# Reference: these 'string' versions without RE are from this link:
# https://stackoverflow.com/a/48350803
def replace_all(
    needle: Sequence, haystack: Sequence, volunteer: Sequence = ""
) -> Sequence:
    """ return a sequence with all `needles` in `haystack` replaced with `volunteers` """
    return "".join(volunteer if c in needle else c for c in haystack)


def rep_whitelist(
    needle: Sequence, haystack: Sequence, volunteer: Sequence = ""
) -> Sequence:
    """ return a sequence with all `needles` in `haystack` saved and all other characters replaced with `volunteers` """
    return "".join(volunteer if c not in needle else c for c in haystack)


def make_safe_id(haystack: Sequence, volunteer: Sequence = "_") -> Sequence:
    """ return a string that  only alphanumeric and _ characters.

        others are replaced with `volunteer` (default `_`) """
    return "".join(volunteer if not c.isidentifier() else c for c in haystack)


def my_list(list):
    """ shortened version of `join` method """

    @property
    def join(self, s=" "):
        return s.join(self).strip()
