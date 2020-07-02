#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 'future imports'
from __future__ import absolute_import

# 'Standard Library'
import ast
import os

# 'package imports'
from _version import __version__

# 'third party'
from setuptools import find_namespace_packages, setup

from os import (  # platform specific newline; platform specific path separator
    linesep as NL, sep as PATHSEP,)



# appdirs is a dependency of setuptools, so allow installing without it.
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


# path for this script
_SCRIPT_PATH: str = os.path.dirname(__file__)

# app file info (assuming directory name matches app)
_APP_NAME: str = os.path.basename(_SCRIPT_PATH)
_APP_FILE: str = _APP_NAME + ".py"
_APP_PATH: str = os.path.join(_SCRIPT_PATH, _APP_NAME)

print(f"{_SCRIPT_PATH=}")
print(f"{_APP_NAME=}")
print(f"{_APP_FILE=}")
print(f"{_APP_PATH=}")


def get_path(fname: str) -> str:
    """ Return full path of file <fname> in *current* script directory.

    `get_path(fname: str)-> str`

    """
    return os.path.join(_SCRIPT_PATH, fname)


def read(fname: str, nl: str = NL) -> str:
    """ #### Return file contents with normalized line endings.

        `read(fname: str)-> str`

        Return text of file <fname> with line endings normalized to "\\n"

            fname:  str - name of file to process
            nl:     str - default newline string ('\\n')

            return: str - text of file <fname>
        """
    with open(get_path(fname)) as inf:
        out = nl + inf.read().replace("\r\n", nl)
    return out


def get_version(fname: str) -> str:
    """ #### Get version from file <fname>.

        `get_version(fname: str) -> str`

        """
    for line in read(fname).splitlines():
        if line.startswith("__version__"):
            version = ast.literal_eval(line.split("=", 1)[1].strip())
            return version
    return ""


# Do not import `appdirs` yet, lest we import some random version on sys.path.
version = get_version("_version.py")

_dev_mode_: bool = True

if _dev_mode_:
    print("Running setup for {} version {}...".format(_APP_FILE, version))
else:
    setup(
        name="appdirs",
        version=version,
        description="A small Python module for determining appropriate "
        + 'platform-specific dirs, e.g. a "user data dir".',
        long_description=read("README.rst") + "\n" + read("CHANGES.rst"),
        python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: Implementation :: PyPy",
            "Programming Language :: Python :: Implementation :: CPython",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ],
        keywords="application directory log cache user",
        author="Trent Mick",
        author_email="trentm@gmail.com",
        maintainer="Trent Mick; Sridhar Ratnakumar; Jeff Rouse",
        maintainer_email="trentm@gmail.com; github@srid.name; jr@its.to",
        url="https://github.com/ActiveState/appdirs",
        license="MIT",
        py_modules=["appdirs"],
    )


def setup_attrs(
    name: str,
    version: str,
    description: str,
    long_description: str,
    author: str,
    author_email: str,
    maintainer: str,
    maintainer_email: str,
    url: str,
    download_url: str,
    packages: List[str],
    py_modules: List[str],
    scripts: List[str],
    ext_modules: List[Extension],
    classifiers: List[str],
    distclass: Type[Distribution],
    script_name: str,
    script_args: List[str],
    options: Mapping[str, Any],
    license: str,
    keywords: Union[List[str], str],
    platforms: Union[List[str], str],
    cmdclass: Mapping[str, Type[Command]],
    data_files: List[Tuple[str, List[str]]],
    package_dir: Mapping[str, str],
    obsoletes: List[str],
    provides: List[str],
    requires: List[str],
    command_packages: List[str],
    command_options: Mapping[str, Mapping[str, Tuple[Any, Any]]],
    package_data: Mapping[str, List[str]],
    include_package_data: bool,
    libraries: List[str],
    headers: List[str],
    ext_package: str,
    include_dirs: List[str],
    password: str,
    fullname: str,
    **attrs: Any,
) -> None:
    pass


"""
setup(
    name=__title__,
    version=__version__,
    description="System utilities for Python on macOS",
    long_description=open("README.md").read(),
    __author__="Michael Treanor",
    __author_email__="skeptycal@gmail.com",
    __author__="Michael Treanor",
    __author_email__="skeptycal@gmail.com",
    url=f"https://skeptycal.github.io/{__title__}/",
    license=__license__,
    packages=find_namespace_packages(),
    install_requires=["tox", "pytest", "coverage", "pytest-cov"],
    test_suite="test",
    zip_safe=False,
    keywords="cli utilities python ai ml text console log debug test testing",
    package_data={
        # If any package contains txt, rst, md files, include them:
        "": ["*.txt", "*.rst", "*.md", "*.ini", "*.png", "*.jpg"]
    },
    project_urls={
        "Website": "https://skeptycal.github.io/{__title__}/",
        # "Documentation": "https://docs.example.com/HelloWorld/",
        "Source Code": "https://www.github.com/skeptycal/{__title__}/",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: MacOS X",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Programming Language :: Cython",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
    ],
)
"""
