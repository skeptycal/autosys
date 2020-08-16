#!/usr/bin/env python3
""" Part of the [AutoSys][1] package

    Copyright (c) 2018 [Michael Treanor][2]

    AutoSys is licensed under the [MIT License][3]

    [1]: https://www.github.com/skeptycal/autosys
    [2]: https://www.twitter.com/skeptycal
    [3]: https://opensource.org/licenses/MIT
    """

from os import PathLike, linesep as NL
from pathlib import Path
from pprint import pformat

import toml

from toml import TomlDecodeError

from typing import Any, Dict, MutableMapping, MutableSequence, Union


class _Error(Exception):
    def __init__(self, message, errors):
        import traceback

        # Call Exception.__init__(message)
        # to use the same Message header as the parent class
        # super().__init__(message)
        self.errors = errors
        # Display the errors
        print('There were some errors:')
        print(self.errors)
        # print(pformat(traceback.format_exc(limit=1)))


class TomlParserError(_Error):
    """ An error occurred while processing a toml file. """

# Reference: https://www.learnpython.dev/03-intermediate-python/40-exceptions/90-custom-exceptions/


class GitHubApiException(Exception):

    def __init__(self, status_code):
        if status_code == 403:
            message = "Rate limit reached. Please wait a minute and try again."
        else:
            message = f"HTTP Status Code was: {status_code}."

        super().__init__(message)


def my_name(self):
    import inspect
    try:
        return inspect.stack()[1][3]
    except:
        return -1


class TomlParser(MutableMapping):

    def __init__(self, filename: PathLike = '', toml_data: MutableMapping[str, Any] = {}) -> None:
        self._filename: Path = None
        self._data: str = None

        # grab the inputs and lazyload everything else
        self._inputfile: PathLike = filename
        self._inputdata: Any = toml_data

        if self._inputfile:
            self = self.load()

    @property
    def filename(self) -> Path:
        """ Return the Path of the toml file (default _inputfile) """
        if not self._filename:
            self._filename = Path(self._inputfile).resolve()
        return self._filename

    @filename.setter
    def filename(self, f: PathLike) -> int:
        """ Set the Path of the toml file. """
        if Path(f).is_file():
            self._filename = Path(f).resolve()
            return 0
        return 1

    @property
    def data(self, m: MutableMapping[str, Any] = {}) -> str:
        """ translate from dict to toml string """
        if not self._data:
            if not m:
                m = str(self._inputdata)
            else:
                self._data = toml.dumps(m)
        return self._data

    def to_dict(self, s: str) -> MutableMapping[str, Any]:
        """ translate from toml string to dict """
        if not self:
            self = toml.loads(s)
        return dict(self)

    def save(self) -> int:
        try:
            with self.filename.open(mode='wt') as fd:
                toml.dump(self.data, fd)
        except Exception as e:
            raise TomlDecodeError(
                f"{my_name()}: Error reading toml file <{self.filename.name}>.")

    def load(self, f: PathLike) -> MutableMapping[str, Any]:
        try:
            if f:
                self.filename(f)
                self = toml.load(self.filename)
        except Exception as e:
            raise

    def __str__(self) -> str:
        if self.data:
            return pformat(self.to_dict())
        return ''


def main(test: bool = False):
    if test:
        try:
            i = 1/0
        except Exception as e:
            raise TomlParserError('There were some errors:', e)


main(False)
