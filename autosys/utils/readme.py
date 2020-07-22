#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" readme.py

    locate and return the project's readme file

    ---
    Part of the [AutoSys][1] package

    Copyright (c) 2018 [Michael Treanor][2]

    AutoSys is licensed under the [MIT License][3]

    [1]: https://www.github.com/skeptycal/autosys
    [2]: https://www.twitter.com/skeptycal
    [3]: https://opensource.org/licenses/MIT
    """

# 'Standard Library'
from pathlib import Path

try:
    DEFAULT_ENCODING
except:
    from locale import getpreferredencoding

    DEFAULT_ENCODING: str = getpreferredencoding(do_setlocale=True) or "utf-8"


def readme(filename: str = "readme.md"):
    """ Returns the text of the README file

        The default file is `README.md` and is *NOT* case sensitive. (e.g. `README` is the same as `readme`)
        Can load *any* text file, but the default search path is setup for readme files

        ```
        Search path = ["readme.md", "readme.rst", "readme", "readme.txt"]
        ```

        Example:

        ```
        long_description=readme()
        ```
        """

    search_list = ["readme.md", "readme.rst", "readme", "readme.txt"]
    if filename not in search_list:
        search_list.insert(0, filename)
    found: bool = False
    for searchfile in search_list:
        for parent in Path(__file__).resolve().parents:
            find_path = Path(parent / searchfile)
            if find_path.exists():
                found = True
                print(find_path)
                break
        if found:
            break
    if found:
        try:
            with open(find_path, mode="r", encoding=DEFAULT_ENCODING) as f:
                return f.read()
        except IOError as e:
            return e
    else:
        raise FileNotFoundError(
            f"Cannot find project 'readme' file in project tree. Search list = {search_list}"
        )
