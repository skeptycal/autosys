

def __getattr__(name):
    import importlib
    if name in __all__:
        return importlib.import_module("." + name, __name__)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def get_class_name(_name, verbose=True):
    """ Alternate class name function with optional formatting """
    _cls_name = eval(f"{_name}.__class__.__name__")
    if not verbose:
        return _cls_name
    return f"{_name} - <class '{_cls_name}'>"

# generic test class for `add_method`
A = type("A", (object, ), dict(a=1))


def add_method(cls):
    """ Decorator to add method to class 'cls' """
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            return func(*args, **kwargs)

        setattr(cls, func.__name__, wrapper)
        # Note we are not binding func, but wrapper which accepts self but does exactly the same as func
        return func  # returning func means func can still be used normally

    return decorator


# Samples


# Decorator can be written to take normal functions and make them methods. These functions still act as normal if passed a standard variable. If they are passed a method parameter, they are run as class methods with 'self' injected in as needed
@add_method(A)
def foo():
    print("hello world!")


@add_method(A)
def bar(s):
    print(f"Message: {s}")
