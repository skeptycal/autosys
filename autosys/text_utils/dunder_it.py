def dunder_it(string: str,
              fill_spaces: bool = True,
              ignore_errors: bool = True) -> (str, Exception):
    ''' Return name `string` with dunder prefix and suffix added if needed.

        fill_spaces - if True, replace spaces with '_'

        ignore_errors - if True, return empty string on errors

        e.g.
        ```
        NL -> __NL__
        the_variable -> __the_variable__
        __doc__ -> __doc__
        ```
        '''
    try:
        return f"__{str(string).replace(' ','_').lstrip(' _').rstrip(' _')}__"
    except Exception as e:
        if ignore_errors:
            return ""  # skip errors
        return e  # return errors
