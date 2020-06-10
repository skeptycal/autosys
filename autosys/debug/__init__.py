#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Part of the `AutoSys` package
        copyright (c) 2019 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """



""" Error alternates:

    class _Enum_ish(tuple):
        # alternate Enum:
        # ref: https://stackoverflow.com/a/9201329
        __getattr__ = tuple.index
        __setattr__ = None
        __del__ = None


    class _Enum_like(object):
        # alternate Enum
        # ref: https://stackoverflow.com/a/4092436
        values = []

        class __metaclass__(type):
            def __getattr__(self, name):
                return self.values.index(name)

            def name_of(self, i):
                # There's another handy advantage: really fast reverse lookups:
                return self.values[i]

    """
""" GOALS:
    By creating this app, I wanted to answer these questions:

    - What are the internet activities that I use or want most often?
    - What are the things that are feasible, but that I cannot easily do?

    Here is a list of items I came up with. I have solved them to some degree, but any advice or suggestions is welcome. See Contributors document for information.

    1. "Give me the information I want or need to do a better job."
    2. "Store data for later use ... I haven't thought of the question yet."
    3. "Encrypt and Secure data."

    - Create a map of variables, functions, and errors
    - Include links to manual descriptions
    - Convert to a 3d object
    - Create a "developer log" with timestamps in a database
        - Interact with underlying database
        - Used to generate timelines of error tracing
        - "The detective novels of coding."
    - Disable certain features on the fly (decorator?)
    - Disable or interact with certain trackers / loggers
    - Track file io and database io
    - Use this data to "auto-Mock" a database of test features
    - Search for English (or language) words and separate them from tags
    - Test for API functionality
    - Create "auto-API"
    """
