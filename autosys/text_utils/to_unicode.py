import sys

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3
PY38 = sys.version_info[0:2] >= (3, 8)

# only Python3 is supported now ...
if PY3:
    string_types = str,
    integer_types = int,
    class_types = type,
    text_type = str
    binary_type = bytes
    from sys import maxsize as MAXSIZE
""" else:
        string_types = basestring,
        integer_types = (int, long)
        class_types = (type, types.ClassType)
        text_type = unicode
        binary_type = str

        if sys.platform.startswith("java"):
            # Jython always uses 32 bits.
            MAXSIZE = int((1 << 31) - 1)
        else:
            # It's possible to have sizeof(long) != sizeof(Py_ssize_t).
            class X(object):
                def __len__(self):
                    return 1 << 31

            try:
                len(X())
            except OverflowError:
                # 32-bit
                MAXSIZE = int((1 << 31) - 1)
            else:
                # 64-bit
                MAXSIZE = int((1 << 63) - 1)
            del X """


def force_unicode(text):
    """Takes a text (Python 2: str/unicode; Python 3: unicode) and converts to unicode

    :arg str/unicode text: the text in question

    :returns: text as unicode

    :raises UnicodeDecodeError: if the text was a Python 2 str and isn't in
        utf-8

    """
    # If it's already unicode, then return it
    if isinstance(text, six.text_type):
        return text

    # If not, convert it
    return six.text_type(text, 'utf-8', 'strict')
