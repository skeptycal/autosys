#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minimal Python Module Setup File
Requires Python 3.7 (dataclass support)
"""
from setuptools import setup
from dataclasses import dataclass
from typing import List
# set default package name to parent folder name


@dataclass()
class SetupConfig:
    name: str = __file__.split('/')[-2]
    version: str = '0.0.1'
    description: str = name + ' - utility for macOS'
    url: str = 'http://github.com/skeptycal/' + name
    author: str = 'Michael Treanor'
    author_email: str = 'skeptycal@gmail.com'
    license: str = 'MIT'
    packages = []
    zip_safe: bool = False


s = SetupConfig(version='0.1')

print(s)
print()


# setup(name=name,
#       version='0.1',
#       description=description,
#       url='http://github.com/skeptycal/xxxx',
#       author='Michael Treanor',
#       author_email='skeptycal@gmail.com',
#       license='MIT',
#       packages=['xxxx'],
#       zip_safe=False)
