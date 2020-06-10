#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Regex Extract
    ---
    ReExtract - A wrapper class to process a regex pattern, apply to a text file, and return the first string match. Optionally, a default may be used when no match is found. Logging and error handling are included.

    `file_name` (required str) - a text io stream containing the `pattern`

    `pattern` (optional re.Pattern) - a precompiled regex `pattern`

    `search_string` (optional str) - a raw string containing a regex pattern

    `flags` (optional int) - flags used for regex operations

    `default` (optional str) - a default value returned if `pattern` is not found

    Example:
    ```
    RE_VERSION: re.Pattern = re.compile(
        pattern= r'^__version__\s?=\s?[\'"]([^\'"]*)[\'"]',
        flags=DEFAULT_RE_FLAGS)

    result = ReExtract(
        file_name="VERSION.txt",
        pattern=RE_VERSION,
        default="0.0.1"
        )

    ```

    No Pattern Provided
    ---

    If no `pattern` is provided, a re.Pattern object is created from the `search_string` and `flags` arguments. Otherwise, these two arguments are ignored. (flags are not available at all when passing a precompiled re.Pattern object since they are compiled into the re.Pattern object.)

    Example:
    ```
    result = ReExtract(
        file_name="VERSION.txt",
        search_string=r'^__version__\s?=\s?[\'"]([^\'"]*)[\'"]',
        flags=re.MULTILINE | re.IGNORECASE
        default="0.0.1"
        )

    ```
    Errors:
    ---
    - if there is a file error, `Re_File_Error` is raised
    - if there is a matching error, the `default` is returned
    - if there is a matching error and no default is provided, a `Re_Value_Error` is raised

    AutoSys
    ---
    Part of the [AutoSys][1] package

    Copyright (c) 2018 [Michael Treanor][2]

    AutoSys is licensed under the [MIT License][3]

    [1]: https://www.github.com/skeptycal/autosys
    [2]: https://www.twitter.com/skeptycal
    [3]: https://opensource.org/licenses/MIT
    """

import autosys.regex_utils
from autosys.regex_utils import *


@dataclass(repr=False)
class ReExtract:
    """ Regex Extract
        ---
        A wrapper class to process a regex pattern, apply to a text file, and return the first string match. Optionally, a default may be used when no match is found. Logging and error handling are included.

        `file_name` (required str) - a text io stream containing the `pattern`

        `pattern` (optional re.Pattern) - a precompiled regex `pattern`

        `search_string` (optional str) - a raw string containing a regex pattern

        `flags` (optional int) - flags used for regex operations

        `default` (optional str) - a default value returned if `pattern` is not found

        Example:
        ```
        RE_VERSION: re.Pattern = re.compile(
            pattern= r'^__version__\s?=\s?[\'"]([^\'"]*)[\'"]',
            flags=DEFAULT_RE_FLAGS)

        result = ReExtract(
            file_name="VERSION.txt",
            pattern=RE_VERSION,
            default="0.0.1"
            )

        ```

        No Pattern Provided
        ---

        If no `pattern` is provided, a re.Pattern object is created from the `search_string` and `flags` arguments. Otherwise, these two arguments are ignored. (flags are not available at all when passing a precompiled re.Pattern object since they are compiled into the re.Pattern object.)

        Example:
        ```
        result = ReExtract(
            file_name="VERSION.txt",
            search_string=r'^__version__\s?=\s?[\'"]([^\'"]*)[\'"]',
            flags=re.MULTILINE | re.IGNORECASE
            default="0.0.1"
            )

        ```
        Errors:
        ---
        - if there is a file error, `Re_File_Error` is raised
        - if there is a matching error, the `default` is returned
        - if there is a matching error and no default is provided, a `Re_Value_Error` is raised

        AutoSys
        ---
        Part of the [AutoSys][1] package

        Copyright (c) 2018 [Michael Treanor][2]

        AutoSys is licensed under the [MIT License][3]

        [1]: https://www.github.com/skeptycal/autosys
        [2]: https://www.twitter.com/skeptycal
        [3]: https://opensource.org/licenses/MIT
        """

    file_name: str
    pattern: re.Pattern = None
    default: str = ""
    search_string: str = ""
    flags: int = DEFAULT_RE_FLAGS
    _result: Field = field(default="", init=False)
    _path_name: Field = field(Path(), init = False)
    def __post_init__(self):
        if not self.pattern:
            self.pattern = re.compile(pattern=self.pattern, flags=self.flags)
        self._path_name = Path(self.file_name).resolve()

    def _get_file_contents(self, as_list: bool = False) -> (str, List):
        """ Return text file contents as one string.

            as_list - if True, return contents as a list of lines

            Wrapper for logging and error handling of file opening. """
        fh: TextIOWrapper = None
        try:
            with open(self.file_name, "rt") as fh:
                log.info(f"Opening file '{self.file_name}' go get contents.")
                if as_list:
                    log.info(
                        f"Returning list of lines from text file '{self.file_name}'."
                    )
                    return fh.readlines()
                log.info(f"Returning contents of text file '{self.file_name}'.")
                return fh.read()
        except Exception as e:
            msg = f"File error while opening file '{self.file_name}'{NL}{e.args}"
            log.error(msg, e)
            raise Re_File_Error(msg, e)

    def _re_get_file_data(self) -> (str):
        """ Return the first match for regex `pattern` from `file_name`
        else `default` if it exists. """
        data: str = self._get_file_contents()
        try:
            result = self.pattern.search(data).groups()[0] or self.default
        except (ValueError, KeyError, AttributeError, TypeError) as e:
            if self.default:
                return self.default
            raise Re_Value_Error(
                f"Pattern '{pattern}' not found in file '{file_name}'", e
            )
        except Exception as e:
            log(e)
            raise Re_Value_Error(
                f"Error occurred while searching for pattern '{pattern}' in file '{file_name}'",
                e,
            )
        finally:
            return str(result)

    def __str__(self):
        if not self._result:
            self._result = self._re_get_file_data()
        return str(self._result)
