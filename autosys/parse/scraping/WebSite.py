# 'Standard Library'
import sys

from contextlib import closing

# 'package imports'
# from webpage import *
import webpage

from bs4 import BeautifulSoup

# 'third party'
import requests

from requests import (
    Response,
    get,
)
from requests.exceptions import RequestException

from typing import List

_debug_: bool = True


def get_mathematicians():
    # example use case
    url = "http://www.fabpedigree.com/james/mathmen.htm"
    w = WebSite(url)
    print(w)
    html = BeautifulSoup(WebSite(url), "html.parser")

    for i, li in enumerate(html.select("li")):
        print(i, li.text)


def _test_(args):
    for url in args:
        w = webpage.WebPage(url)
        w = WebSite(url)
        r = w.resp
        print(w)
        print(r)
        print(w.is_html(r))
        print(w.encoding)
        print(w.resp.encoding)
        print(w.resp.apparent_encoding)
        print()
        get_mathematicians()

        content_type = w.resp.headers["Content-Type"].lower()
        print(content_type)
        print(w.resp.headers["Content-Type"].lower())


def _main_(args: List):
    """
    CLI script main entry point.
    """
    url = "https://realpython.com/blog/"
    if _debug_:
        args.extend(url)
        _test_(args)


if __name__ == "__main__":  # if script is loaded directly from CLI
    _main_(sys.argv[1:])
