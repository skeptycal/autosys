#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# !---------------------------------------------- Custom Types


class Const:
    """ A wrapper that makes variables constant. """

    def __init__(self, val, report_errors=True):
        super(Const, self).__setattr__("value", val)
        self.report_errors: bool = report_errors

    def __setattr__(self, name, val):
        if self.report_errors:
            raise ValueError("Trying to change a constant value!", self)

    def __str__(self):
        return str(self.value)


class _Struct(type):
    """ A custom structure that can have any fields defined. """

    # Ref: https://stackoverflow.com/questions/35988/c-like-structures-in-python

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class _MapDict(dict):
    """ A custom dictionary that autoloads it's kwargs. """

    def __init__(self, **kwargs):
        super(_MapDict, self).__init__(**kwargs)
        self.__dict__ = self


class _KwargStruct(type):
    """ A custom type that creates instance variables from args and kwargs.

        e.g.
        ```
        class MyClass(object):
        ''' An example custom class based on _KwargStruct. '''
        __metaclass__ = _KwargStruct

        def __init__(self, a, b, c):
            pass
        ```
        """

    def __call__(cls, *args, **kwargs):
        names = cls.func_code.co_varnames[1:]

        self = type.__call__(cls, *args, **kwargs)

        for name, value in zip(names, args):
            setattr(self, name, value)

        for name, value in kwargs.items():
            setattr(self, name, value)
        return self


def _init_all_args(fn):  # TODO --- not working (renamed as _xxx)
    """ A custom decorator used to wrap __init__ in custom classes in
        order to create instance variables from args and kwargs.

        e.g.
        ```
        class Test(object):
        @init_all_args
        def __init__(self, a, b):
            pass
        ```
        """

    @wraps(fn)
    def wrapped_init(self, *args, **kwargs):
        """ TODO --- AttributeError: 'function' object has no attribute 'func_code' """

        names = fn.func_code.co_varnames[1:]
        print(f"{names=}")
        vprint('names')

        for name, value in zip(names, args):
            setattr(self, name, value)

        for name, value in kwargs.items():
            setattr(self, name, value)

    return wrapped_init

# Singleton/BorgSingleton.py
# Alex Martelli's 'Borg'


class Borg:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class Singleton(Borg):
    def __init__(self, arg):
        Borg.__init__(self)
        self.val = arg

    def __str__(self): return self.val


stuff = 'the stuff'
other_stuff = 'the other stuff'
vprint('stuff', 'other_stuff')
