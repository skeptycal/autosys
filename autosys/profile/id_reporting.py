import re
from os import linesep as NL

RE_DEFAULT_BITE_SIZE = 5
RE_DEFAULT_FLAGS = re.MULTILINE
RE_NUM = fr"\d{{1-{RE_DEFAULT_BITE_SIZE}}}*"
print(RE_NUM)


def brk(x):
    return re.findall(RE_NUM, x)


def breakup(s, bite_size=3, divider=" "):
    tmp = ""
    for i, c in enumerate(str(s)):
        tmp += c
        if (i + 1) % bite_size == 0:
            tmp += divider
    return tmp


def id_tail(x: object, n: int = 5) -> (str):
    return str(id(x))[-n:]
