from typing import Dict, List, Sequence, Tuple


def dict_str(ignore_errors=True, sort_items=True, **kwargs):
    """ Return string from an iterable of variously typed arguments. Each item is converted separately, allowing errors in individual items to be ignored.

        data: iterable - iterable containing items
        arg_sep: str   - separator between list items

        ignore_errors  - Errors in types and formatting are ignored.
        """
    tmp: List[str] = []
    for k, v in kwargs:
        try:
            if isinstance(v, dict):
                v = dict_str(
                    ignore_errors=ignore_errors, sort_items=sort_items, **v
                )
            tmp.append(f"{k}: {v}")
        except:
            pass
    if sort_items:
        tmp = sorted(tmp)


def arg_str(*data, arg_sep: str = "", ignore_errors=True, **kwargs):
    """ Return string from an iterable of variously typed arguments. Each item is converted separately, allowing errors in individual items to be ignored.

        data: iterable - iterable containing items
        arg_sep: str   - separator between list items

        ignore_errors  - Errors in types and formatting are ignored.
        """
    tmp: List[str] = []
    for arg in data:
        try:
            tmp.append(str(arg))
        except:
            pass

    if len(data) == 0 or data == None:
        return ""


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


if __name__ == "__main__":
    tmp: Dict = dict(globals())
    print(tmp)
#    for k, v in tmp.items():
#       try:
#           print(k, v)
#       except:
#           pass
