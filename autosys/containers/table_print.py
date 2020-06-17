from os import linesep as NL
from typing import Dict, Sequence


def table_print(data: (Dict, Sequence), **kwargs):
    tmp: List = []
    if isinstance(data, dict):
        tmp.extend(
            [f"{str(k):<15.15} :  {repr(v):<45.45}" for k, v in data.items()])
    elif isinstance(data, (list, tuple, set)):
        for x in data:
            try:
                tmp.append(f"{str(x):<15.15} :  {repr(f'{x}'):<45.45}")
            except:
                tmp.append(f"{str(x)}")
    else:
        raise TypeError('Parameter must be an iterable Mapping or Sequence.')
    print(NL.join(tmp), **kwargs)
