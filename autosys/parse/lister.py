#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Tests for Autosys package. For more information:
https://docs.python-guide.org/writing/tests/
"""

from typing import Iterable

# from autosys.debug import *
from autosys.cli.debug import ARGS, NL, br, dbprint, hr

_debug_: bool = True  # True => use Debug features
__all__ = ["Lister"]


class Lister(list):
    DEV_BLACKLIST = ("_", "arepl")
    """ Utility to return various formats of an iterable. """
    # TODO - add textwrap functionality

    def __init__(self, iterable):
        super().__init__(iterable)
        self.data = list(iterable)

    def __all__(self):
        return [f"{x}" for x in self.filter(blacklist=Lister.DEV_BLACKLIST)]

    def __str__(self):
        return self.comma

    def join(self, sep=" ") -> str:
        return sep.join(self)

    @property
    def lines(self, wrap=79) -> str:
        return NL.join(self)

    @property
    def comma(self) -> str:
        return ", ".join(self)

    @property
    def sort(self, rev=False):
        return Lister(sorted(self._list, reverse=rev))

    @property
    def len(self) -> int:
        try:
            return len(self)
        except IndexError:
            return 0

    @property
    def size(self):
        return Lister(self._list)

    # @property
    # def max(self):
    #     return self._list.max()

    def bl(self, blacklist=DEV_BLACKLIST):
        return Lister([x for x in self._list if not x.startswith(blacklist)])

    def wl(self, whitelist=("")):
        return Lister([x for x in self._list if x.startswith(whitelist)])

    def filter(self, blacklist=DEV_BLACKLIST, whitelist=("")):
        """ Return the list containing only `whitelist` items that are not `blacklist` items.

            blacklist - items that are tossed out. defaults:
                - '__' : 'dundermethods'
                - '_' : 'dunders' and private variables
                - 'arepl' : (dev) from the AREPL VsCode Extension 

            whitelist - items that are retained if not blacklisted. defaults:
                - '' : default to return all

            Notes:
                - '' as item in whitelist returns all (use as default)
                - () as blacklist returns all (use as default)

                - '' as item in blacklist returns nothing (edge case)
                - () as whitelist returns nothing (edge case)
            """
        # testing for these edge cases likely imposes significant performance
        # costs, especially the blacklist check. That one is avoided.
        if whitelist == ():
            return self.bl(blacklist=blacklist)
        # if '' in blacklist:
        #     return self.wl(whitelist=whitelist)
        return Lister(
            list(
                [
                    x
                    for x in self
                    if x.startswith(whitelist) and not x.startswith(blacklist)
                ]
            )
        )


_lister = Lister(dir())
__all__ = Lister(dir()).__all__()
# print(__all__)


def _tests_():
    """ Debug Tests for script. """
    br()
    d = _lister

    # print(d.max)
    # hr()
    # print(d.len)
    # hr()
    print(d.join())
    # br()
    # print(d.comma)
    br()
    # print(d.wl())
    print(d.filter())
    print(d.__all__())
    print(d.lines)
    br()
    del d


def _main_():  # !------------------------ Script Main
    """
    CLI script main entry point.
    """
    if _debug_:
        _tests_()


if __name__ == "__main__":
    _main_()
