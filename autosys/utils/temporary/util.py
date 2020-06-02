import errno

import contextlib2 as contextlib


@contextlib.contextmanager
def allow_missing_file():
    try:
        yield
    except OSError as e:
        if e.errno != errno.ENOENT:
            raise
