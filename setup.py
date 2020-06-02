#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" `AutoSys` package
        copyright (c) 2018 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """


import os
import re
from setuptools import setup, find_packages


from autosys.utils.readme import readme


def version(path: str = "VERSION.txt") -> str:
    with open(path, "r") as file:
        # this is a string like __version__ = 'x.x.x'
        RE_VERSION = r'^__version__\s?=\s?[\'"]([^\'"]*)[\'"]'
        return re.match(RE_VERSION, file.read(), re.MULTILINE)[0].split("'")[1]


"""
def readme(file_name: str = "README.md") -> str:
    with open(file_name, "rb") as file:
        return file.read().decode("utf-8")
"""


def name():
    return "autosys"


print(version())
if True:
    setup(
        name=name(),
        version=version(),
        description="System utilities for Python on macOS",
        python_requires=">=3.8",
        packages=find_packages(),
        py_modules=["autosys"],
        license="MIT license",
        long_description=readme(),
        long_description_content_type="text/markdown",
        # long_description_content_type="text/x-rst",
        author="Michael Treanor",
        author_email="skeptycal@gmail.com",
        maintainer="Michael Treanor",
        maintainer_email="skeptycal@gmail.com",
        keywords=[
            "application",
            "macOS",
            "dev",
            "devops",
            "cache",
            "utilities",
            "cli",
            "python",
            "cython",
            "text",
            "console",
            "log",
            "debug",
            "test",
            "testing",
            "logging",
            "logger",
        ],
        url=f"https://skeptycal.github.io/{name}/",
        download_url=f"https://github.com/skeptycal/{name}/archive/{version}.tar.gz",
        zip_safe=False,
        package_data={
            # If any package contains these files, include them:
            "": [
                "*.txt",
                "*.rst",
                "*.md",
                "*.ini",
                "*.png",
                "*.jpg",
                "__init__.pyi",
                "py.typed",
            ]
        },
        project_urls={
            "Website": f"https://skeptycal.github.io/{name}/",
            "Documentation": f"https://skeptycal.github.io/{name}/docs",
            "Source Code": f"https://www.github.com/skeptycal/{name}/",
            "Changelog": "https://github.com/skeptycal/{name}/blob/master/CHANGELOG.md",
        },
        install_requires=[
            "colorama>=0.3.4 ; sys_platform=='win32'",
            "aiocontextvars>=0.2.0 ; python_version<'3.7'",
            "win32-setctime>=1.0.0 ; sys_platform=='win32'",
        ],
        extras_require={
            "dev": [
                "black>=19.3b0 ; python_version>='3.8'",
                "codecov>=2.0.15",
                "colorama>=0.3.4",
                "flake8>=3.7.7",
                "isort>=4.3.20",
                "tox>=3.9.0",
                "tox-travis>=0.12",
                "pytest>=4.6.2",
                "pytest-cov>=2.7.1",
                "Sphinx>=2.2.1",
                "sphinx-autobuild>=0.7.1",
                "sphinx-rtd-theme>=0.4.3",
            ]
        },
        classifiers=[
            "Development Status :: 4 - Beta",
            "License :: OSI Approved :: MIT License",
            "Environment :: Console",
            "Environment :: MacOS X",
            "Intended Audience :: Developers",
            "Natural Language :: English",
            "Operating System :: MacOS",
            "Operating System :: OS Independent",
            "Programming Language :: Cython",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3 :: Only",
            "Programming Language :: Python :: 3",
            # These are the Python versions tested; it may work on others
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: Implementation :: CPython",
            "Programming Language :: Python :: Implementation :: PyPy",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Topic :: Software Development :: Testing",
            "Topic :: Utilities",
        ],
    )
