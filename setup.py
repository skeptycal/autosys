#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import

if True: # stdlib imports
    import os
    import sys
    import ast                      # safer eval ...
    from os import linesep as NL    # platform specific newline
    from os import sep as PATHSEP   # platform specific path separator
    from typing import *            # >= 3.6 type hints support

if True: # setup tools
    from setuptools import find_namespace_packages, setup
    from autosys._version import *

    _debug_: bool = True
    DEFAULT_VERSION_FILE='_version.py'
    def dbprint(*db_args, sep='', end='', file=sys.stderr, flush=False):
        ''' Prints debug messages if _debug_ flag is True.

            The default <sep> and <end> are empty strings which allows for easier custom formatting. Change the defaults as needed.

            Example:
            ```py
            if arg == '--version':
                dbprint(f"anansi.py version {Ansi.lime}{__version__}.")
            ```
            '''
        if _debug_:
            print(f"{sep.join(*db_args)}{NL}",
                sep=sep, end=end, file=file, flush=flush)


class PyApp():

    def __init__(self,
                 dev: bool = False,
                 version: str = __version__,
                 lic: str = __license__,
                 python_requires: str =__python_requires__,
                 author: str = __author__,
                 author_email: str = __author_email__,
                 keywords: str = __keywords__
                 ):
        self._install_path:  str = os.path.dirname(__file__).lower()
        self._name: str = os.path.basename(self._install_path).lower()
        self._main: str = f"{self.name}.py"
        self._app_path: str = os.path.join(self._install_path, self.name)
        self._version_file: str = os.path.join(
            self._app_path, DEFAULT_VERSION_FILE)

        # key parameters (must be present)
        self.dev: bool = dev
        self._version: str = version

        # direct parameters
        self.license: str = lic
        self.author: str = author
        self.author_email: str = author_email
        self.python_requires: str = python_requires
        self.maintainer: str = self.author
        self.maintainer_email: str = self.author_email

    def get_path(self,fname: str) -> str:
        """ Return full path of file <fname> in *current* script directory.

        `get_path(fname: str)-> str`

        """
        if self.dev:
            dbprint(f"getpath returns: {os.path.join(self._install_path, fname)}")
        return os.path.join(self._install_path, fname)

    def read(self, fname: str) -> str:
        """ #### Return file contents with normalized line endings.

            `read(fname: str)-> str`

            Return text of file <fname> with line endings normalized to "\\n"

                fname:  str - name of file to process
                nl:     str - default newline string ('\\n')

                return: str - text of file <fname>
            """
        with open(self.get_path(fname)) as inf:
            return inf.read().replace("\r\n", NL)

    def _get_version(self) -> str:
        """ #### Get package version from file <self._version_file>.

            `example:`
            `self.version = self.get_version()`

            """
        if __version__:
            self._version = __version__
            return __version__
        else:
            for line in self.read(self._version_file).splitlines():
                if line.startswith("__version__"):
                    version = ast.literal_eval(line.split("=", 1)[1].strip())
                    self._version = version
                    return version
        return ''

    def _dev_report(self):
        print(f"Running setup for {self.name} version {self.version}")
        print(f"{self._install_path=}")
        print(f"{self._name=}")
        print(f"{self._main=}")
        print(f"{self._app_path=}")
        print(f"{self._version_file=}")
        print(f"{self._version=}")

    @property
    def name(self):
        return self._name
    @property
    def version(self):
        return self._version if self._version else self._get_version()
    @property
    def readme(self):
        self.read('README.rst') + NL + self.read('CHANGES.rst')


app = PyApp(dev=True)

app._dev_report()
print(app.name)

if _debug_:
    print(f"Running setup for {app.name} version {app.version}")
else:
    setup(
            name=app.name,
            version=app.version,
            description='A small Python module for determining appropriate ' + \
                'platform-specific dirs, e.g. a "user data dir".',
            long_description=app.readme,
            python_requires=app.python_requires,
            classifiers=[
                'Development Status :: 5 - Production/Stable',
                'Intended Audience :: Developers',
                'License :: OSI Approved :: MIT License',
                'Operating System :: OS Independent',
                'Programming Language :: Python',
                'Programming Language :: Python :: 2',
                'Programming Language :: Python :: 2.7',
                'Programming Language :: Python :: 3',
                'Programming Language :: Python :: 3.5',
                'Programming Language :: Python :: 3.6',
                'Programming Language :: Python :: 3.7',
                'Programming Language :: Python :: 3.8',
                'Programming Language :: Python :: Implementation :: PyPy',
                'Programming Language :: Python :: Implementation :: CPython',
                'Topic :: Software Development :: Libraries :: Python Modules',
            ],
            keywords=app.keywords,
            author=app.author,
            author_email=app.author_email,
            maintainer=app.maintainer,
            maintainer_email=app.maintainer_email,
            url=app.url,
            license=app.license,
            packages=find_namespace_packages(),
            py_modules=list(self.name),
        )




"""
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
    ext_modules: List[str],
    classifiers: List[str],
    distclass: Type[str],
    script_name: str,
    script_args: List[str],
    options: Mapping[str, Any],
    license: str,
    keywords: Union[List[str], str],
    platforms: Union[List[str], str],
    cmdclass: Mapping[str, str],
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
