import os
import tempfile

import pathlib2 as pathlib
import contextlib2 as contextlib

import temporary.util


@contextlib.contextmanager
def temp_file(
        content=None,
        suffix='',
        prefix='tmp',
        parent_dir=None):
    """
    Create a temporary file and optionally populate it with content. The file
    is deleted when the context exits.

    The temporary file is created when entering the context manager and
    deleted when exiting it.
    >>> import temporary
    >>> with temporary.temp_file() as temp_file:
    ...     assert temp_file.exists()
    >>> assert not temp_file.exists()

    The user may also supply some content for the file to be populated with:
    >>> with temporary.temp_file('hello!') as temp_file:
    ...     with temp_file.open() as f:
    ...         assert f.read() == 'hello!'

    The temporary file can be placed in a custom directory:
    >>> with temporary.temp_dir() as temp_dir:
    ...     with temporary.temp_file(parent_dir=temp_dir) as temp_file:
    ...         assert temp_file.parent == temp_dir

    If, for some reason, the user wants to delete the temporary file before
    exiting the context, that's okay too:
    >>> with temporary.temp_file() as temp_file:
    ...     temp_file.unlink()
    """
    binary = isinstance(content, (bytes, bytearray))
    parent_dir = parent_dir if parent_dir is None else str(parent_dir)
    fd, abs_path = tempfile.mkstemp(suffix, prefix, parent_dir, text=False)
    path = pathlib.Path(abs_path)
    try:
        try:
            if content:
                os.write(fd, content if binary else content.encode())
        finally:
            os.close(fd)
        yield path.resolve()
    finally:
        with temporary.util.allow_missing_file():
            path.unlink()
