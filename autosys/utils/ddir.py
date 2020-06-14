# 'Standard Library'
from os import linesep as NL

from typing import (
    Any,
    Dict,
    List,
)


def ddir(
    thing_string: str,
    indent: int = 2,
    skip_dunders: bool = True,
    skip_builtins: bool = True,
    skip_join: bool = True,
) -> (List, str):
    result: List = []
    value: str = ""

    try:
        thing = eval(f"{thing_string}")
        thing
    except:
        raise

    thing = thing_string

    try:
        getattr(thing, __iter__)
        iter_thing = thing
    except:
        iter_thing = dir(thing)
    # print('iter_thing: ', iter_thing)
    for k in iter_thing:
        # print(f'{thing}.k: ', k)
        if skip_dunders and k.startswith("_"):
            continue
        if isinstance(k, (dict, list)):
            value = ddir(k)
        else:
            try:
                value = eval(k)
                if str(value).startswith("<func"):
                    if skip_builtins:
                        continue
                    value = f"<function {k}>"
                # assert False
            except:
                try:
                    evl = f"{thing_string}.{k}"
                    # print(evl)
                    value = eval(f"{evl}()")
                except:
                    try:
                        value = eval(f"{evl}")
                        # value = str(value)
                        # print("no parens eval: ", value)
                        if str(value).startswith("<built-in"):
                            if skip_builtins:
                                continue
                            value = f"<builtin: '{k}'>"
                    except:
                        try:
                            value = str(value)
                            print(value)

                        except:
                            pass
                        #     value = f"{k}"
                        #     if value.startswith("<meth"):
                        #         value = f"<method {k}>"
                        # except:
                        #     value = f"<{k}>"

        result.append(f"{indent*' '}{k:<15.15}: {value}")
        if not skip_join:
            result = NL.join(result)
    return result
