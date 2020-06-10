#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Part of the `AutoSys` package - utilities for macOS apps
        copyright (c) 2019 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """


class StrSubclass(str):
    def __getitem__(self, index):
        return StrSubclass(super().__getitem__(index))


class BytesSubclass(bytes):
    def __getitem__(self, index):
        return BytesSubclass(super().__getitem__(index))
