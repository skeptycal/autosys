#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


if True:  # * >>-------------------------------->> Exception utilities.

    def produce_exception(recursion_level=2):
        sys.stdout.flush()
        if recursion_level:
            produce_exception(recursion_level - 1)
        else:
            raise RuntimeError()

    def call_function(f, recursion_level=2):
        if recursion_level:
            return call_function(f, recursion_level - 1)
        else:
            return f()


if True:  # * >>-------------------------------->> Base Package Exception

    class Error(Exception):
        """ Base error class for subclassign. """

        def __init__(self, message):
            self.message = message

            Exception.__init__(self, message)


if True:  # * >>-------------------------------->> Specific Package Exceptions

    class SetupError(ValueError):
        """ An error occurred with the module setup parameters. """

    class Re_File_Error(ValueError):
        """ There was a file error while attempting to match the pattern. """

    class Re_Value_Error(ValueError):
        """ A regex matching error occurred. """

    class BaseFileError(IOError):
        """ There was a problem initializing the file object. """

        pass


if True:  # * >>----------------------------------->> bump2version exceptions
    # from https://github.com/c4urself/bump2version

    class IncompleteVersionRepresentationException(Error):
        pass

    class MissingValueForSerializationException(Error):
        pass

    class WorkingDirectoryIsDirtyException(Error):
        pass

    class MercurialDoesNotSupportSignedTagsException(Error):
        pass


if True:  # * >>---------------------------->> python 3.8 regex base exception
    pass
    '''
    # The regex exception.
    class error(Exception):
        """Exception raised for invalid regular expressions.

        Attributes:

            msg: The unformatted error message
            pattern: The regular expression pattern
            pos: The position in the pattern where compilation failed, or None
            lineno: The line number where compilation failed, unless pos is None
            colno: The column number where compilation failed, unless pos is None
        """

        def __init__(self, message, pattern=None, pos=None):
            newline = "\n" if isinstance(pattern, str) else b"\n"
            self.msg = message
            self.pattern = pattern
            self.pos = pos
            if pattern is not None and pos is not None:
                self.lineno = pattern.count(newline, 0, pos) + 1
                self.colno = pos - pattern.rfind(newline, 0, pos)

                message = "{} at position {}".format(message, pos)

                if newline in pattern:
                    message += " (line {}, column {})".format(self.lineno, self.colno)

            Exception.__init__(self, message)
        '''
