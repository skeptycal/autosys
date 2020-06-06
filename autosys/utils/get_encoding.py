def get_encoding():
    from locale import getpreferredencoding

    try:
        return getpreferredencoding(do_setlocale=True) or "utf-8"
    except:
        return "utf-8"


DEFAULT_ENCODING: str = get_encoding()
