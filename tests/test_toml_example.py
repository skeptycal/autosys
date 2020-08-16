#!/usr/bin/env python3
""" Part of the [AutoSys][1] package

    Copyright (c) 2018 [Michael Treanor][2]

    AutoSys is licensed under the [MIT License][3]

    [1]: https://www.github.com/skeptycal/autosys
    [2]: https://www.twitter.com/skeptycal
    [3]: https://opensource.org/licenses/MIT
    """

from os import PathLike
from pathlib import Path
from pprint import pformat

import toml

from toml import TomlDecodeError

from typing import Any, Dict, MutableMapping, MutableSequence, Union


class _Error(Exception):
    def __init__(self, *args, **kwargs):
        import traceback
        s = traceback.format_exc()
        super().__init__(self, s, *args, **kwargs)


class TomlParserError(_Error):
    """ An error occurred while processing a toml file. """


def my_name(self):
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


def main():
    try:
        assert True == False
    except Exception as e:
        raise TomlParserError(e)


main()
