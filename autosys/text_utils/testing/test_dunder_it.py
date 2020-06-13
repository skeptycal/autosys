from autosys.text_utils.dunder_it import dunder_it


def test_dunder_it_dict():
    test_list_answer_key = {
        'name with spaces': '__name_with_spaces__',
        'leading spaces': '__leading_spaces__',
        'trailing spaces': '__trailing_spaces__',
        'List': '__List__',
        'NL': '__NL__',
        'NUL': '__NUL__',
        'STR_ALPHA': '__STR_ALPHA__',
        'STR_ALPHANUMERIC': '__STR_ALPHANUMERIC__',
        'STR_HEX': '__STR_HEX__',
        'STR_NAMES': '__STR_NAMES__',
        'STR_PRINTABLE': '__STR_PRINTABLE__',
        'STR_PUNCTUATION': '__STR_PUNCTUATION__',
        'STR_WHITESPACE': '__STR_WHITESPACE__',
        'Sequence': '__Sequence__',
        '__builtins__': '__builtins__',
        '__doc__': '__doc__',
        '__file__': '__file__',
        '__loader__': '__loader__',
        '__name__': '__name__',
        '__package__': '__package__',
        'a': '__a__',
        'arepl_store': '__arepl_store__',
        'b': '__b__',
        'difference': '__difference__',
        'help': '__help__',
        'howdoi': '__howdoi__',
        'input': '__input__',
        'random_string': '__random_string__',
        'string': '__string__',
    }

    for q, a in test_dunder_it_dict.items():
        assert dunderit(q) == a
