#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" mathematicians.py - sample web scraping script
    (reference: https://realpython.com/python-web-scraping-practical-introduction/)

        copyright (c) 2019 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal
    """

if True:  # ! -- System Imports
    import sys
    from pprint import pprint
    from contextlib import closing

if True:  # ! -- Third Party Imports
    from requests import get
    from requests.exceptions import RequestException
    from bs4 import BeautifulSoup

    try:
        import lxml

        DEFAULT_PARSER = "lxml"
    except:
        DEFAULT_PARSER = "html.parser"

    # from autosys import *

# !---------------------------------------------- Common CONSTANTS
_debug_: bool = False
_fuzzy_: bool = True

DEFAULT_URL_HISTORY: int = 1000

# !---------------------------------------------- Custom Types


class ScrapeError(Exception):
    pass


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers["Content-Type"].lower()
    return (resp.status_code == 200 and content_type is not None
            and content_type.find("html") > -1)


def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)


def get_p_tags(html):
    for p in html.select("p"):
        yield p.text


def soup(url):
    return BeautifulSoup(simple_get(url), DEFAULT_PARSER)


# !---------------------------------------------- Script Tests
def __tests__(args) -> (int):
    """ Run Debug Tests for script if _debug_ = True. """

    print(f"{DEFAULT_PARSER=}")
    url = "https://realpython.com/blog/"
    raw_html = simple_get(url)
    html = soup(url)
    pprint(html)
    return 0


def __main__(args) -> (int):
    """ CLI script main entry point. """

    #! script testing
    if _debug_:
        __tests__(args)
    return 0


if __name__ == "__main__":  # if script is loaded directly from CLI
    __main__(sys.argv[1:])
""" Notes
    from tutorial ... moved out of __test__()

    raw_html = simple_get("https://realpython.com/blog/")
    print(len(raw_html))

    no_html = simple_get("https://realpython.com/blog/nope-not-gonna-find-it")

    print(no_html is None)

    # raw_html = open("contrived.html").read()
    """
