import logging
import os
from dataclasses import dataclass
from pathlib import Path, _posix_flavour, _windows_flavour

from autosys.implore.text import TextMessaging


@dataclass(frozen=True)
class Verbosity:
    """ Reports output of the selected level and below. """

    V_CRITICAL: int = 50  # Serious error - unable to continue
    V_ERROR: int = 40  # Failure of essential function
    V_WARN: int = 30  # Show Warnings of possible problems
    V_INFO: int = 20  # brief normal reporting
    V_DEBUG: int = 10  # detailed reporting for debugging

    # these next three are equivalent ... choice is good
    # logger messages will be forwarded with this setting
    # all other messages will be shown
    V_QUIET: int = 0
    V_NONE: int = 0
    V_STFU: int = 0


@dataclass(frozen=True)
class LogLevel:
    """ Logging Levels Numeric values.
        https://docs.python.org/3.9/library/logging.html#levels
        """

    LOG_CRITICAL: int = 50  # Serious error - unable to continue
    LOG_ERROR: int = 40  # Failure of essential function
    LOG_WARNING: int = 30  # Show Warnings of possible problems
    LOG_INFO: int = 20  # brief normal reporting
    LOG_DEBUG: int = 10  # detailed reporting for debugging

    # logger messages will be forwarded with this setting
    # all other messages will be shown
    LOG_NOTSET: int = 0


@dataclass
class DevConfig:
    """ Handle exceptions and logging for development. """

    debug: bool = True
    log_flag: bool = True
    re_raise: bool = True
    send_texts: bool = True
    send_emails: bool = True
    send_to_stderr: bool = True

    verbose: Verbosity = Verbosity.V_DEBUG
    log_level: LogLevel = LogLevel.LOG_DEBUG

    def __post_init__(self):
        if self.log_flag:
            self.logger = logging.getLogger(__name__)
        if self.send_texts:
            self.tm = TextMessaging()

    def log(e: Exception):
        """ Log an exception based on configuration. """
        self.logger()

    def e(e: Exception):
        """ Handle exceptions based on configuration. """
        pass

    def dev(e: Exception):
        pass


dev = DevConfig()


class PathFinder(Path):
    _flavour = _windows_flavour if os.name == "nt" else _posix_flavour

    def __init__(self, filename):
        super().__init__()
        self._path = Path(filename).resolve()
        print(self._path)
        self._filename = self._path.name
        self._create_file()
        print(self._filename)

        self._headers = []
        # _post_init allows the standard `init` to be left alone
        #   - cleaner for interited classes
        #   - handy for dataclasses
        self._post_init()

    def _post_init(self):
        pass

    def _create_file(self):
        if self.exists():
            print("exists")
        else:
            print("does not exist ... creating")
            try:
                self.touch()
            except Exception as e:
                log(e)
                dev(e)

        print(self._filename)
        return self._filename

    def rename(self, name):
        self._name = name
        return self._name

    @property
    def name(self):
        if not self._name:
            self._name = Path(filename).basename()
        return self._name

    @property
    def get_cwd(self) -> Path:
        return self.cwd().resolve()

    @property
    def basename(self) -> str:
        _file = Path(filename).basename()


class MarkdownFile(PathFinder):
    def __init__(*args, **kwargs):
        self._headers = []
        super.__init__(*args, **kwargs)

    def headers():
        # path = pathlib.Path.cwd() / 'test.md'
        if not self._headers:
            with open(self, mode="r") as fid:
                self._headers = [
                    line.strip() for line in fid if line.startswith("#")
                ]
        return self._headers
        # print('\n'.join(headers))


class PythonFile(PathFinder):
    def headers():
        # path = pathlib.Path.cwd() / 'test.py'
        if not self._headers:
            with open(self, mode="r") as f:
                self._headers = [
                    line.strip() for line in f if line.startswith("#")
                ]
        return self._headers
        # print('\n'.join(headers))


if __name__ == "__main__":
    p = PathFinder("faketest")
