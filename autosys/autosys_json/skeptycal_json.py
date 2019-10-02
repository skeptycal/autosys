#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##############################################################################
# """ module skeptycal_json.py """
# features in this module:
#   _json_translation_table - print python to json translation tables
#   json_read               - open and read data into python object
#   json_write              - write json object to file and sort if needed
#   json_sort               - sort list of python files as json objects
#   json_minify             - compact json files and remove comments
#   json_pretty_print       - format 'pretty print' style
##############################################################################
# Imports
if True:  #! stupid trick to make collapsing secions easier in VSCode
    import os
    import sys
    import pathlib
    import re
    import fileinput

    # from collections import OrderedDict
    from io import StringIO
    from typing import Any, Dict, List, Tuple, Union

    # from logging import Logger

    # fix import path for non standard libraries
    sys.path.append(os.path.dirname(os.path.realpath(__file__)))
    # Use speedup if available
    # scanstring = c_scanstring or py_scanstring
    try:
        import ujson as json  # Speedup if present; no big deal if not
    except ImportError:
        import json

##############################################################################
# constants
DEBUG_FLAG: bool = True
ENCODING: str = "utf8"
##############################################################################
# general functions
def db_print(*args, **kwargs):
    """ db_print - print to console only if debug flag is set """
    if DEBUG_FLAG:
        print(*args, **kwargs)


def is_file(file_name: str) -> bool:
    if pathlib.Path(file_name).is_file():
        return True
    else:
        return False


##############################################################################
# json functions
class JSON_file(object):
    io = StringIO()
    file_name: str = ""
    json_data: Any = None
    path_name = ""
    pattern_name = ""
    encoding: str = ENCODING

    def __init__(self, *args, **kwargs):
        self.encoding = ENCODING
        super().__init__(*args, **kwargs)

    def set_file(self, json_file: str) -> bool:
        if is_file(json_file):
            self.file_name = json_file
            return True
        else:
            return False

    def error_handler(self, e: Exception):
        # TODO add error handling ...
        return False

    def _json_translation_table(self) -> str:
        # Reference: https://docs.python.org/3/library/json.html#json-to-py-table
        """
            _json_translation_table : return json -> python translation table
                result (str)        : string containing formatted table
            """
        result = """     json translations for python

            Reference:
                https://docs.python.org/3/library/json.html

                ╔═══════════════════════════════╗
                ║    class json.JSONDecoder     ║
                ║    (Simple JSON decoder)      ║
                ╠═════════════════╦═════════════╣
                ║  JSON           ║  Python     ║
                ╠═════════════════╬═════════════╣
                ║  object         ║  dict       ║
                ║  array          ║  list       ║
                ║  string         ║  str        ║
                ║  number (int)   ║  int        ║
                ║  number (real)  ║  float      ║
                ║  true           ║  True       ║
                ║  false          ║  False      ║
                ║  null           ║  None       ║
                ╚═════════════════╩═════════════╝

                ╔═══════════════════════════════╗
                ║    class json.JSONEncoder     ║
                ║    (Simple JSON encoder)      ║
                ╠═════════════════╦═════════════╣
                ║  Python         ║  JSON       ║
                ╠═════════════════╬═════════════╣
                ║  dict           ║  object     ║
                ║  list, tuple    ║  array      ║
                ║  str            ║  string     ║
                ║  int,float,etc  ║  number     ║
                ║  True           ║  true       ║
                ║  False          ║  false      ║
                ║  None           ║  null       ║
                ╚═════════════════╩═════════════╝
        """
        return result

    def json_comments(self, comments):
        if not comments:
            self.json_data = json.loads(
                "".join(line for line in data_file if not line.startswith("//"))
            )

    def json_read(self) -> bool:
        """
            json_read: load a json file and remove comments if needed
                (comments are not officially allowed in json format)

            parameter:
                json_file (str)     : file to load
                comments (bool)     : comments are allowed? (default False)
            return:
                result (object)     : on success - python json object from json_file
                                    : error code if failure
            """
        try:
            with open(self.file_name, "r") as data_file:
                self.json_data = json.load(self.file_name)
                return True
        except (OSError, IOError, ValueError) as e:
            return False

    def json_write(self) -> bool:
        """
            json_write: write json object to file and sort if needed

            parameter:
                json_file (str)     : file name used to write json_data
                json_data (object)  : json data as python object
                is_sorted (bool)    : sort keys alphabetically (default True)
            return:
                result (int)     : 0 for success else error code
            """
        try:
            with open(self.file_name, "w", encoding=self.encoding) as data_file:
                data_file.write(self.json_data)
            return True
        except (OSError, IOError, ValueError) as e:
            self.error_handler(e)
            return False

    def json_format(
        self,
        comments: bool = False,
        sort_keys: bool = True,
        separators: Tuple[str, str] = (", ", ": "),
        indent: Union[int, str] = 4,
        ensure_ascii: bool = False,
        skipkeys: bool = False,
        check_circular: bool = True,
    ) -> bool:
        try:
            self.json_data = json.dumps(
                self.file_name,
                sort_keys=sort_keys,
                separators=separators,
                indent=indent,
                ensure_ascii=ensure_ascii,
                skipkeys=skipkeys,
                check_circular=check_circular,
            )
            return True
        except (OSError, IOError, ValueError) as e:
            self.error_handler(e)
            return False

    def json_sort(self, comments: bool = False) -> bool:
        """
            json_sort: alphabetize json files and remove comments if needed

            parameter:
                comments (bool)     : comments are allowed? (default False)
            return:
                result (bool)       : True if successful else False
            """
        return self.json_format(self, comments=True)

    def json_minify(self, comments: bool = False) -> bool:
        """
            json_minify: compact json data and remove comments

            parameter:
                comments (bool)     : comments are allowed? (default False)
            return:
                result (bool)       : True if successful else False
            """
        return self.json_format(
            self, comments=False, sort_keys=False, separators=(",", ":"), indent=None
        )

    def json_pretty_print(self, comments: bool = False) -> str:
        """
            json_pretty_print: format json for pretty printing

            parameter:
                comments (bool)     : comments are allowed? (default False)
            return:
                result (str)        : json file as formatted string
            """
        return self.json_format(self, comments=True, sort_keys=False)


##############################################################################
# CLI testing
if __name__ == "__main__":  # If run as CLI utility
    args: List[str] = []
    TEST_FILE: str = "/Volumes/Data/skeptycal/bin/utilities/python/test.json"

    j: JSON_file = JSON_file()
    j.file_name = TEST_FILE
    print(j.file_name)
    # if j.json_read(TEST_FILE):
    #     j.json_pretty_print()
    #     print(j.json_data)

    class arg_choice(object):
        name: str = ""
        args: List[str] = []

        def __init__(self, *args, **kwargs):
            self.name = sys.argv[0]
            self.args = sys.argv[1:]
            super().__init__(*args, **kwargs)

        def parse(self):
            for arg in self.args:
                self.indirect(arg)

        def indirect(self, i):
            method_name = "number_" + str(i)
            method = getattr(self, method_name, lambda: "Invalid")
            db_print("indirect method_name: ", method_name)
            db_print("indirect method: ", method)
            return method()

        def number_0(self):
            return "zero"

        def number_1(self):
            return "one"

        def number_2(self):
            return "two"

    if len(sys.argv) > 1:
        args = sys.argv[1:]
    else:
        args = [TEST_FILE.__str__()]

    db_print()
    db_print("args: ", args[:])
    db_print("is_file({}): {}".format(args[0], is_file(args[0])))

    a: object = arg_choice()
    a.parse()

    print("a.indirect: ", a.indirect(1))

    db_print()
    # db_print (json_pretty_print(args[0]))
    db_print()

    # result = json_sort(args)
