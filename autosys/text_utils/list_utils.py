from typing import Sequence


def replace_all(
    needle: Sequence, haystack: Sequence, volunteer: Sequence = ""
) -> Sequence:
    """ return a sequence with all `needles` in `haystack` replaced with `volunteers` """
    return "".join(volunteer if c in needle else c for c in haystack)


def rep_whitelist(
    needle: Sequence, haystack: Sequence, volunteer: Sequence = ""
) -> Sequence:
    """ return a sequence with all `needles` in `haystack` saved and all other characters replaced with `volunteers` """
    return "".join(volunteer if c not in needle else c for c in haystack)


def make_safe_id(haystack: Sequence, volunteer: Sequence = "_") -> Sequence:
    """ return a string that has only alphanumeric and _ characters.

        others are replaced with `volunteer` (default `_`) """
    return "".join(volunteer if not c.isidentifier() else c for c in haystack)
