#!/usr/bin/env python
from __future__ import absolute_import
from .version import __version__ as version
from setuptools import setup

import version
setup(
    name='sys-py',
    # version=version.__version__,
    description='System utilities for Python on macOS',
    long_description=open('README.md').read(),
    author='Michael Treanor',
    author_email='skeptycal@gmail.com',
    maintainer='Michael Treanor',
    maintainer_email='skeptycal@gmail.com',
    url='http://github.com/skeptycal/sys-py/',
    license='MIT',
    packages=['sys-py'],
    install_requires=[],
    test_requore=['tox', 'pytest', 'coverage', 'pytest-cov'],
    test_suite="test",
    zip_safe=False,
    keywords='cli utilities python ai ml text console log debug test testing',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: MacOS X',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Framework :: Django',
        'Environment :: Web Environment',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Programming Language :: Cython',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Unix Shell',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities'
    ]
)
