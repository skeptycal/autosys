#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 'Standard Library'
import re

regex = r"\A[\w\s:\-<>\(\)\+\*]+\Z"
regex = r"\A[\w\s:\-<>\(\)\+\*\&\@]+\Z"
regex = r"[^\w\s\-\(\)\>\^\<\&\@\!\:\+\=\*]"

REGEX_SAFE_STRING = r"[^\w\s\-\(\)\>\^\<\&\@\!\:\+\=\*\'\"]"
RE_SAFE_STRING = re.compile(REGEX_SAFE_STRING, re.IGNORECASE | re.MULTILINE)
# https://regex101.com/r/9YvEas/1

RE_FLAGS_DEBUG = re.IGNORECASE | re.MULTILINE | re.VERBOSE | re.DEBUG

test_str = (
    "def fibonacci_2(n: int) -> int:\n"
    "    if n > 1:\n"
    "        return fibonacci(n - 1) + fibonacci(n - 2)\n"
    "    else:\n"
    "        return n=^&*(@@!)"
)

matches = re.search(
    regex, test_str, re.IGNORECASE | re.MULTILINE | re.VERBOSE | re.DEBUG
)


def is_safe(s) -> bool:
    return re.search(
        RE_SAFE_STRING, s, re.IGNORECASE | re.MULTILINE | re.VERBOSE | re.DEBUG
    )


print(matches)
# if matches:
#     print("Match was found at {start}-{end}: {match}".format(
#         start=matches.start(), end=matches.end(), match=matches.group()))

#     for groupNum in range(0, len(matches.groups())):
#         groupNum = groupNum + 1

#         print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum,
#                                                                         start=matches.start(groupNum), end=matches.end(groupNum), group=matches.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
