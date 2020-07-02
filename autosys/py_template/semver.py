# 'Standard Library'
import re

from os import linesep as NL
from pprint import pprint

RE_SEMVER_PCRE_STRING: str = r"^(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"

RE_SEMVER_ECMA_STRING: str = r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"

# default flags
#   - ignore case
#   - allow matches on any line to count

# Do NOT use these defaults if you have other needs
RE_DEFAULT_FLAGS: re.RegexFlag = re.IGNORECASE | re.MULTILINE

RE_SEMVER_PCRE: re.Pattern = re.compile(
    RE_SEMVER_PCRE_STRING, flags=RE_DEFAULT_FLAGS
)
RE_SEMVER_ECMA: re.Pattern = re.compile(
    RE_SEMVER_ECMA_STRING, flags=RE_DEFAULT_FLAGS
)


def is_semver(s: str) -> (bool):
    """ Return True if the given string is a valid SEMVER string. """
    return re.fullmatch(RE_SEMVER_ECMA, s) is not None


def contains_semver(s: str) -> (bool):
    """ Return True if the given string contains a valid SEMVER string. """
    return re.search(RE_SEMVER_ECMA, s) is not None


def get_version_only(s: str) -> (re.Match, None):
    """ Return the first match of a SEMVER string in order to remove extraneous labels like 'version=' from version """
    return re.search(RE_SEMVER_PCRE, s)


p = RE_SEMVER_PCRE.groups
e = RE_SEMVER_ECMA.groups


v1 = "2.1.0"
isv = is_semver(v1)
sv = get_version_only(v1)

print(isv)
print(sv)


print()
print(p)
print(e)
print(is_semver("not_semver"))
print(is_semver("2.1.0"))
print(is_semver("version: 2.1.0"))
print(contains_semver("version: 2.1.0"))
print(get_version_only("version: 2.1.0"))
