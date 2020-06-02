from pathlib import Path

def read(filename: str, ignore_errors: bool = False):
    """ Returns the text of `filename`.

        filename: str       - name of file to read and return
        ignore_errors: bool - ignore all errors and return None instead
        """
    log.info(f"function `read` with args {filename=} and {ignore_errors=}.")
    try:
        file_path = Path(__file__).resolve().parents[0] / filename
        log.info(f"read from: {file_path}")  # debug
        with open(file_path, encoding=DEFAULT_ENCODING) as f:
            return f.read()
    except (OSError, NameError, TypeError) as e:
        if not ignore_errors:
            return e
    return None
