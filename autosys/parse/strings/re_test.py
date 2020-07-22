#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 'Standard Library'
import re

regex1 = r"\A[\w\s:\-<>\(\)\+\*]+\Z"
regex2 = r"\A[\w\s:\-<>\(\)\+\*\&\@]+\Z"
regex3 = r"[^\w\s\-\(\)\>\^\<\&\@\!\:\+\=\*]"

REGEX_SAFE_STRING = r"[^\w\s\-\(\)\>\^\<\&\@\!\:\+\=\*\'\"]"
RE_SAFE_STRING = re.compile(REGEX_SAFE_STRING, re.IGNORECASE | re.MULTILINE)

# https://regex101.com/r/9YvEas/1

RE_FLAGS_DEBUG = re.IGNORECASE | re.MULTILINE | re.VERBOSE | re.DEBUG

test_str = ("def fibonacci_2(n: int) -> int:\n" +
            "    if n > 1:\n" +
            "        return fibonacci(n - 1) + fibonacci(n - 2)\n" +
            "    else:\n" +
            "        return n=^&*(@@!)")

matches = re.search(string=test_str, pattern=RE_SAFE_STRING)


def is_safe(s) -> (bool):
    return re.search(string=s, pattern=RE_SAFE_STRING) == True


def return_matches(s, joined=True):
    tmp = [x for x in s if x in REGEX_SAFE_STRING]
    if joined:
        return ''.join(tmp)
    return tmp


def _mat(s, p, x):
    if s in p:
        return x
    return s


def remove_matches(s, joined=True):
    tmp = [_mat(x, REGEX_SAFE_STRING, '')
           for x in s.strip()]
    if joined:
        return ''.join(tmp)
    return tmp


def replace_matches(s, joined=True):
    tmp = ''.join([_mat(x, REGEX_SAFE_STRING, '_')
                   for x in s.strip()]).splitlines()
    if joined:
        return '\n'.join(tmp).strip(' _')
    return tmp


print(test_str)
print('---------------------------')

print(return_matches(test_str))
print('---------------------------')
print(remove_matches(test_str))
print('---------------------------')
print(replace_matches(test_str))
# print(is_safe(test_str))
