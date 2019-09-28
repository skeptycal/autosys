#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" module d2md """
# alphabetize json files
#   provide file(s) as a list

import json
import sys
from typing import Dict, List
import text_colors

HEADER = color_encode("COLOR15", "BG_BLACK", "ITALIC")
MAIN = color_encode("MAIN", "BG_BLACK", "ITALIC")
BLUE = color_encode("COOL", "BG_BLACK", "ITALIC")
PURPLE = color_encode("PURPLE", "BG_BLACK", "ITALIC")
RESET = color_encode("RESET", "RESET", "RESET")


def to_json(text: str) -> Dict:
    """ Convert text string to json """
    text.rstrip(",")
    rawfile = (line for line in text if line[0] not in ["/", "#"])
    raise NotImplementedError


def sort_json(
    json_files: List[str], comments: bool = False, delim: str = ","
) -> List[str]:
    """
        sort_json: alphabetize json files and remove comments if needed

        parameter:
            json_files (list)   : 1 or more files to sort
            comments (bool)     : comments are allowed? (default False)
            delim (str)         : delimiter used for input files (default ",")
        return:
            result (list)       : list of failures (empty = success)
        """
    from pathlib import Path

    result = []
    for file in json_files:
        p = Path(file)
        try:
            with p.open(mode="r") as file:
                # read file contents into buffer 'raw_file'
                raw_file = "\n".join(
                    [
                        line.strip()
                        for line in file
                        if not line.startswith("#") and not line.startswith("//")
                    ]
                )
                alphabetized = json.loads(raw_file)
                with open(file, "w") as w:
                    w.write(
                        json.dumps(
                            alphabetized,
                            separators=(",", ": "),
                            indent=4,
                            sort_keys=True,
                            skipkeys=True,
                        )
                    )
        except OSError:
            # if unable to open file, add current file to error list result
            result.append(file)
    return result


if __name__ == "__main__":
    # * Used if run as CLI utility
    arg = ""
    args = sys.argv[1:]
    # * TEST DATA
    # args = ["/Volumes/Data/skeptycal/bin/utilities/py_imports/test.json"]
    # args = ["/Volumes/Data/skeptycal/Library/'Application Support'/Code/User/settings.json"]
    print(args)
    print(PURPLE)
    print("Output for Json_Sort module:")
    print("MIT license  |  copyright (c) 2018 Michael Treanor")
    print("<https://www.github.com/skeptycal")
    print(BLUE)
    print("List of json files: ")
    print(HEADER, args)
    print()
    result = sort_json(args)
    if result:
        for s in result:
            print(BLUE, "The file ", HEADER, s, sep="")
            print(BLUE, " could not be processed.", sep="")
    else:
        print(BLUE, "Command was successful.", sep="")
    print()
