#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" INI files
    ---
    INI files - utilities for parsing ini files into usable datasets

    An INI file is basically a dictionary of keys and values with headings and comments mixed in.

    The most useful data format that maps INI file format is the Python dictionary, which is nearly identical to the JSON specification.

    In the data format used here, the headings are used as 'keys' in key-value pairs and the 'values' are a dictionary of the actual items. This format is also trivial to translate and export the data into JSON format.

    Example:

    ```
    This .editorconfig file is processed into the dictionary shown below:

    # EditorConfig is awesome: http://EditorConfig.org

    # top-most EditorConfig file
    root = true

    # Tab indentation
    [*]
    indent_style = space
    indent_size = 4
    trim_trailing_whitespace = true
    end_of_line = lf
    insert_final_newline = true

    # Matches multiple files with brace expansion notation
    # Set default charset
    [*.{js,py}]
    charset = utf-8

    # The indent size used in the `package.json` file cannot be changed
    # https://github.com/npm/npm/pull/3180#issuecomment-16336516
    [{.travis.yml,npm-shrinkwrap.json,package.json}]
    indent_style = space
    indent_size = 2
    ```

    Data after processing:

    {
        "top":{
            "root": True,
        },
        "*": {
            "indent_style": "space",
            "indent_size": "4",
            "trim_trailing_whitespace": "true",
            "end_of_line": "lf",
            "insert_final_newline": "true",
        },
        "*.{js,py}":{
            "charset": "utf-8",
        }
    }

        []


    (Comments can optionally be ignored or processed into labels. They are ignored in the above example.)



    AutoSys
    ---
    Part of the [AutoSys][1] package

    Copyright (c) 2018 [Michael Treanor][2]

    AutoSys is licensed under the [MIT License][3]

    [1]: https://www.github.com/skeptycal/autosys
    [2]: https://www.twitter.com/skeptycal
    [3]: https://opensource.org/licenses/MIT
    """
# 'Standard Library'
import io
import re

from dataclasses import (
    Field,
    dataclass,
    field,
)
from pathlib import Path

# 'package imports'
from autosys.log import logging
from autosys.parse import ini_files

from typing import List


''' #TODO - features to add to TextFile
    _access_log: List = field(init=False)
    _track: bool = False
    readlines: bool = True
    '''


class IniFileError(Exception):
    ''' Ini file error. '''


@dataclass
class TextFile:
    file_name: str
    comment_char: str = '#;'
    keep_comments: bool = True
    _raw_data: str = ''
    _path: Path = field(init=False)

    def __post_init__(self):
        self._path = self._get_path(self.file_name)
        self._access_log = []
        self._raw_data = self._get_data()
        if not self.keep_comments:
            self.data = self._drop_comments()

    @staticmethod
    def resolve(path_name: (str, Path)) -> (Path):
        ''' Return a Path that has been resolved and verified. '''
        if Path(path_name).resolve().is_file():
            return Path(path_name).resolve()
        raise IOError(f'The file {path_name} was not found.')

    def _get_path(self, path_name) -> (Path):
        tmp: Path = None
        try:  # try script directory
            return self.resolve(path_name)
        except:
            try:  # try PWD
                return self.resolve(Path().cwd() / Path(path_name).name)
            except:
                raise

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path_name):
        if not self._path:
            self._path = self._get_path(path_name)
        return self._path

    def _get_data(self):
        try:
            with open(self.path, mode='rt') as fd:
                lines = fd.readlines()
        except:
            raise IniFileError(f"Error reading data from file <{self.path}>.")

    def _drop_line_comment(self, line):
        retval = line.split(self.comment_char)[0].strip()
        if retval:
            return retval
        return None

    def _drop_comments(self):
        ''' strip comments and whitespace. '''
        tmp: List = []
        for line in self._raw_data:
            line = self._drop_line_comment(line)
            if line:
                tmp.append(line)
        return tmp

    def as_list(self):
        return [
            f"{k:<20.20}: {v}" for k, v in self.__dict__.items()
            if not k.startswith('_')
        ]

    def pretty(self):
        return '\n'.join(self.as_list())


@dataclass
class IniFile(TextFile):
    heading_pattern: re.Pattern = r'\[.*\]'

    def __post_init__(self):
        super().__post_init__()
        self.readlines = True
        self.find_headings()

    def find_headings(self):
        tmp: List = []
        for line in self._raw_data:
            if re.search(self.heading_pattern, line):
                tmp.append(line.lstrip('[').rstrip(']').strip())
                print(line.lstrip('[').rstrip(']').strip())


s = IniFile(file_name='sample_editorconfig.ini')

print(s.pretty())

# print(sample_ini)

#? -----------------------------------------
#? PyINI
#? https://github.com/PolyEdge/PyINI


class ini:
    class _ini_group:
        def __init__(self, name):
            "Read ini from file object or string given -> ini object"
            self.name = name
            self._items = []

        def __setitem__(self, item, val):
            if type(item) != str:
                raise TypeError("Invalid subscript type")
            for x in range(0, self._items.__len__()):
                if self._items[x][0] == item:
                    self._items[x][1] = val
                    return
            self._items.append([item, val])

        def __getitem__(self, item):
            if type(item) != str:
                raise TypeError("Invalid subscript type")
            for x in range(0, self._items.__len__()):
                if self._items[x][0] == item:
                    return self._items[x][1]
            raise IndexError("Key '" + item + "' not found.")

        def __delitem__(self, item):
            if type(item) != str:
                raise TypeError("Invalid subscript type")
            for x in range(0, self._items.__len__()):
                if self._items[x][0] == item:
                    del self._items[x]
                    return
            raise IndexError("Key '" + item + "' not found.")

        def __iter__(self):
            return iter({x[0]: x[1] for x in self._items if x[0] != -1})

        def __repr__(self):
            return '<ini group {' + (', '.join([
                '"' + str(x[0]) + '": "' + str(x[1]) + '"'
                for x in self._items if x[0] != -1
            ])) + '}>'

        def _add_blank_line(self):
            self._items.append([-1, "blankline"])

        def _add_comment(self, comment):
            self._items.append([-1, "comment", comment])

        def _add_raw(self, raw):
            self._items.append([-1, "raw", raw])

    def __init__(self, ini):
        if type(ini) == io.TextIOWrapper:
            if ini.mode == 'r':
                data = ini.read()
                ini.close()
            else:
                raise ValueError(
                    'File object does not support reading ("r") mode')
        else:
            if type(ini) == str:
                data = ini
            else:
                raise TypeError(
                    'Expected "str" or "io.TextIOWrapper" but got ' +
                    (str(ini.__class__).split()[1][:-1]))
        self._groups = [self._ini_group("__default__")]
        for x in [y.strip() for y in str(data).rsplit(sep='\n')]:
            if x == '':
                self._groups[-1]._add_blank_line()
            elif x[0] == '#':
                self._groups[-1]._add_comment(x[1:])
            elif x[0] == '[':
                self._groups.append(self._ini_group(x[1:-1]))
            elif len(x.split('=', 1)) > 1:
                self._groups[-1][x.split('=', 1)[0].strip()] = x.split(
                    '=', 1)[1].strip()
            else:
                self._groups[-1]._add_raw(x)
        self.create_group = self._create_group
        self.dump = self._dump

    def __setitem__(self, item, val):
        raise TypeError("cannot assign to base ini group")

    def __getitem__(self, item):
        if type(item) != str:
            raise TypeError("Invalid subscript type")
        for x in range(0, self._groups.__len__()):
            if self._groups[x].name == item:
                return self._groups[x]
        raise IndexError("Key '" + item + "' not found.")

    def __delitem__(self, item):
        if type(item) != str:
            raise TypeError("Invalid subscript type")
        for x in range(0, self._groups.__len__()):
            if self._groups[x].name == item:
                del self._groups[x]
                return
        raise TypeError("cannot delete nonexisting ini group.")

    def __iter__(self):
        return iter({x.name: x for x in self._groups})

    def __repr__(self):
        return '<ini group collection [' + (', '.join(
            ['"' + x.name + '"' for x in self._groups])) + ']>'

    def _create_group(self, name):
        for x in range(0, self._groups.__len__()):
            if self._groups[x].name == item:
                raise TypeError("cannot create existing ini group.")
        self._groups.append(self._ini_group(name))

    def _dump(self, stream=None):
        output = []
        for x in self._groups:
            if x.name != '__default__':
                output.append('[' + x.name + ']')
            for y in x._items:
                if (y[0] == -1) and (y[1] == "blankline"):
                    output.append("")
                elif (y[0] == -1) and (y[1] == "comment"):
                    output.append("#" + y[2])
                elif (y[0] == -1) and (y[1] == "raw"):
                    output.append(y[2])
                else:
                    output.append(str(y[0]) + ' = ' + str(y[1]))
        output = '\n'.join(output)
        if stream == None:
            return output
        elif (stream.mode in ['w', 'w+']) and (not stream.closed):
            stream.write(output)
            stream.close()
        elif stream.closed:
            raise IOError('Cannot write to closed stream')
        else:
            raise ValueError('Invalid file mode')


''' sub-class that is inside of class ini '''


class _ini_group:
    def __init__(self, name):
        "Read ini from file object or string given -> ini object"
        self.name = name
        self._items = []

    def __setitem__(self, item, val):
        if type(item) != str:
            raise TypeError("Invalid subscript type")
        for x in range(0, self._items.__len__()):
            if self._items[x][0] == item:
                self._items[x][1] = val
                return
        self._items.append([item, val])

    def __getitem__(self, item):
        if type(item) != str:
            raise TypeError("Invalid subscript type")
        for x in range(0, self._items.__len__()):
            if self._items[x][0] == item:
                return self._items[x][1]
        raise IndexError("Key '" + item + "' not found.")

    def __delitem__(self, item):
        if type(item) != str:
            raise TypeError("Invalid subscript type")
        for x in range(0, self._items.__len__()):
            if self._items[x][0] == item:
                del self._items[x]
                return
        raise IndexError("Key '" + item + "' not found.")

    def __iter__(self):
        return iter({x[0]: x[1] for x in self._items if x[0] != -1})

    def __repr__(self):
        return '<ini group {' + (', '.join([
            '"' + str(x[0]) + '": "' + str(x[1]) + '"'
            for x in self._items if x[0] != -1
        ])) + '}>'

    def _add_blank_line(self):
        self._items.append([-1, "blankline"])

    def _add_comment(self, comment):
        self._items.append([-1, "comment", comment])

    def _add_raw(self, raw):
        self._items.append([-1, "raw", raw])
