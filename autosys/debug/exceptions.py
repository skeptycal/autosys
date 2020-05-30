#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


def produce_exception(recursion_level=2):
    sys.stdout.flush()
    if recursion_level:
        produce_exception(recursion_level - 1)
    else:
        raise RuntimeError()


def call_function(f, recursion_level=2):
    if recursion_level:
        return call_function(f, recursion_level - 1)
    else:
        return f()


# from https://github.com/c4urself/bump2version
class IncompleteVersionRepresentationException(Exception):
    def __init__(self, message):
        self.message = message


class MissingValueForSerializationException(Exception):
    def __init__(self, message):
        self.message = message


class WorkingDirectoryIsDirtyException(Exception):
    def __init__(self, message):
        self.message = message


class MercurialDoesNotSupportSignedTagsException(Exception):
    def __init__(self, message):
        self.message = message
