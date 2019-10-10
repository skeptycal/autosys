#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import

from setuptools import find_namespace_packages, setup

from autosys import version

setup(
    name=version.name,
    version=version.__version__,
    description="System utilities for Python on macOS",
    long_description=open("README.md").read(),
    author="Michael Treanor",
    author_email="skeptycal@gmail.com",
    maintainer="Michael Treanor",
    maintainer_email="skeptycal@gmail.com",
    url="https://skeptycal.github.io/{}/".format(version.name),
    license="MIT",
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
        "Website": "https://skeptycal.github.io/{}/".format(version.name),
        # "Documentation": "https://docs.example.com/HelloWorld/",
        "Source Code": "https://www.github.com/skeptycal/{}/".format(version.name),
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
