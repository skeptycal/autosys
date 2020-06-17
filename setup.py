#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" AutoSys Setup
    ---
    Part of the [AutoSys][1] package

    Copyright (c) 2018 [Michael Treanor][2]

    AutoSys is licensed under the [MIT License][3]

    [1]: https://www.github.com/skeptycal/autosys
    [2]: https://www.twitter.com/skeptycal
    [3]: https://opensource.org/licenses/MIT
    """

# Note: To use the 'upload' functionality of this file, you must:
#   $ pip install twine

import logging
import os
import re

# from dataclasses import Field, dataclass, field
from os import linesep as NL
from pathlib import Path
# from shutil import rmtree as _rmtree
from sys import argv as _argv, path as PYTHONPATH

from setuptools import find_namespace_packages, setup
from typing import Dict, Final, List, Optional, Sequence, Tuple


from package_metadata import *

try:
    DEFAULT_ENCODING
except:
    from locale import getpreferredencoding
    DEFAULT_ENCODING: str = getpreferredencoding(do_setlocale=True) or "utf-8"

#! DEBUG - run some live tests ... set 'False' for production !!!
_debug_: bool = False


here = Path(__file__).resolve().parent

if here not in PYTHONPATH:
    PYTHONPATH.insert(0, here)

logger = logging.getLogger(__name__)


# ? #################################### packaging utilities.
def table_print(data: (Dict, Sequence), **kwargs):
    tmp: List = []
    if isinstance(data, dict):
        tmp.extend(
            [f"{str(k):<15.15} :  {repr(v):<45.45}" for k, v in data.items()])
    elif isinstance(data, (list, tuple, set)):
        for x in data:
            try:
                tmp.append(f"{str(x):<15.15} :  {repr(f'{x}'):<45.45}")
            except:
                tmp.append(f"{str(x)}")
    else:
        raise TypeError('Parameter must be an iterable Mapping or Sequence.')
    print(NL.join(tmp), **kwargs)


def pip_safe_name(s: str):
    """ Return a name that is converted to pypi safe format. """
    return s.lower().replace("-", "_").replace(" ", "_")


def readme(file_name: str = "readme.md"):
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
    if file_name not in search_list:
        search_list.insert(0, file_name)
    found: bool = False
    for searchfile in search_list:
        for parent in Path(__file__).resolve().parents:
            find_path = Path(parent / searchfile)
            if find_path.exists():
                found = True
                # print(find_path)
                break
        if found:
            break
    if found:
        try:
            with open(find_path, mode="r", encoding=DEFAULT_ENCODING) as f:
                return f.read()
        except IOError as e:
            raise IOError(f"Cannot read from the 'readme' file '{find_path}'")
    else:
        raise FileNotFoundError(
            f"Cannot find project 'readme' file in project tree. Search list = {search_list}"
        )


_vars = vars()


def main(args=_argv[1:], ):  # ? ############################## Setup!
    print(f"setup for '{NAME}' version {VERSION}")
    global _debug_
    if 'debug' in args:
        _debug_ = True
    if _debug_:  # do some live tests if setup process has changed ...
        pass
        print(f"{NAME=}")
        print(f"{VERSION=}")
        table_print(_vars)
    else:  # run setup ...
        setup(
            name=NAME,
            version=VERSION,
            description=DESCRIPTION,
            python_requires=REQUIRES_PYTHON,
            package_dir=PACKAGE_DIR,
            packages=find_namespace_packages(
                f'{NAME}', exclude=PACKAGE_EXCLUDE),
            # py_modules=[f"{NAME}"],
            license=LICENSE,
            long_description=LONG_DESCRIPTION,
            long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
            author=AUTHOR,
            author_email=AUTHOR_EMAIL,
            maintainer=MAINTAINER or AUTHOR,
            maintainer_email=MAINTAINER_EMAIL or AUTHOR_EMAIL,
            url=URL,
            download_url=DOWNLOAD_URL,
            zip_safe=ZIP_SAFE,
            include_package_data=INCLUDE_PACKAGE_DATA,
            # setup_requires=["isort"],
            install_requires=REQUIRED,
            extras_require=EXTRAS,
            package_data=PACKAGE_DATA,
            project_urls=PROJECT_URLS,
            keywords=KEYWORDS,
            classifiers=CLASSIFIERS,
        )


if __name__ == "__main__":
    main()
