#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name=name,
    version=__version__,
    description="ANSI text colors for Python",
    long_description=open("README.rst").read(),
    author="Michael Treanor",
    author_email="skeptycal@gmail.com",
    maintainer="Michael Treanor",
    maintainer_email="skeptycal@gmail.com",
    url="http://github.com/skeptycal/textcolors/",
    license="ISC",
    packages=["textcolors"],
    install_requires=[],
    test_requore=["tox", "pytest", "coverage", "pytest-cov"],
    test_suite="test",
    zip_safe=False,
    keywords="ASNI text color style console",
    classifiers=[
        "Environment :: Console",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
