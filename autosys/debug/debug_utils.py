if True:  # !------------------------ config
    import logging
    from pathlib import Path
    from typing import List, Dict
    from autosys.cli import terminal

    _debug_: bool = True  # True => use Debug features
    _verbose_: int = 0  # Verbosity level => 0 - 4
    _log_flag_: bool = _debug_ and True  # True => log to file

    DEBUG_COLOR: str = "\x1B[38;5;178m"  # private ansi CLI color code
    RESET: str = "\x1B[0m"  # private ansi CLI reset code


if True:  # !------------------------ CLI display utilities

    def db_column_ruler(n: int = 5, cols: int = 79):
        """ Print a column ruler of width 'col'. """
        # dbprint('column ruler col: ', col)
        col = cols // n
        dbprint(f'__width:{col:>d}{s80("_", (col - 1) * 10 - 1)}', sep="")
        dbprint("".join([f"         {i}" for i in range(1, col)]))
        dbprint("")
        dbprint(f"1234567890" * (col))
        dbprint(s80("=", col * 10))


# if True:  # !------------------------ Debug Utilities

#     def v_name(**var):
#         """ #### Return the name of a keyword variable as a string.

#             Example:
#             ```
#                 the_value = 'some_value'
#                 print(v_name(the_value=the_value))
#             ```

#             This method is 2x faster than f_name (n = 10000)
#             - 'profile_v_name'  4.98 ms
#             - 'profile_f_name'  10.97 ms

#             >(deprecated: f_name()  :  Return the name of a keyword variable as a string. An alternative to using a list comprehension with function <v_name> that manipulates f-strings directly.)
#             """
#         return [_ for _ in var][0]

#     def tryit(func):
#         """ Decorator to wrap function in a try/except block.

#             Will only catch the first error ... best used for short, quick functions...

#             """
#         def tried(*args, **kwargs):
#             try:
#                 result = func(*args, **kwargs)
#             except Exception as e:
#                 log_it(e)
#                 result = "failed..."
#             else:
#                 # print(args)  # TODO <-- your code here
#                 result = "tried..."
#             finally:
#                 dbprint(result)
#             return result

#         return tried

#     def get_class_name(obj, verbose=True):
#         _cls_name: str = obj.__class__.__name__
#         if not verbose:
#             return _cls_name
#         return f"{_cls_name=}"

# if True:  # !------------------------ Logging Utilities

#     def info(*args):
#         logging.info(*args)

#     def log_error(*args):
#         """ Error reporting in debug mode.

#             current (temporary) behavior: print error messages to <stderr> using dbprint. (if _debug_ flag is True)
#             """
#         # TODO - fix temporary functionality
#         if _log_flag_:
#             logging.info(*args)
#             dbprint(*args)  # ! temp

#     def logex(func):
#         """ Decorator to catch and log errors. """
#         if _log_flag_:
#             try:
#                 result = func()
#             except IOError as e:
#                 log_error(
#                     f"logex caused an error while reporting <{func}>: {e}.")
#             else:
#                 if isinstance(result, Exception):
#                     log_error(f"Function <{func}> caught an error: {e}.")
#             finally:
#                 del e

#     def verbose(v: int, *args, **kwargs):
#         """ Print based on '_verbose_' allowed verbosity level.

#             v: int - requested verbosity level
#             """
#         try:  # if _verbose_ constant does not exist, skip this function
#             _verbose_ == 0
#         except NameError:
#             return -1
#         if _verbose_ >= v:
#             if v < 2:
#                 kwargs["file"] = "sys.stdout"
#                 print(*args, **kwargs)
#             elif v == 2:
#                 kwargs["file"] = "sys.stderr"
#                 print(*args, **kwargs)
