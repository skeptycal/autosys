#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import absolute_import

""" web_basics.py - basic web scraping tools

    copyright (c) 2019 Michael Treanor
    https://www.github.com/skeptycal/autosys
    https://www.twitter.com/skeptycal
    """

import sys
from collections import deque
from contextlib import closing
from dataclasses import dataclass
from logging import Logger
from os import linesep as NL, environ as ENV
from pprint import PrettyPrinter
from sys import argv, stdout, stderr
from typing import Any, Deque, Dict, List, Tuple

from requests import get
from requests.exceptions import RequestException
from bs4 import BeautifulSoup

try:
    import lxml as parser

    DEFAULT_PARSER = "lxml"
except:
    DEFAULT_PARSER = "html.parser"

# from autosys import *


# !---------------------------------------------- Common CONSTANTS
_debug_: bool = True
_fuzzy_: bool = True

DEFAULT_URL_HISTORY: int = 1000

log_web = Logger(__file__)
pp_web = PrettyPrinter(indent=2, width=79, depth=5, stream=stdout, compact=False)

# !---------------------------------------------- Custom Types


class WebPageError(Exception):
    """ An error occured while handling your web document request. """

    this = None


class ScrapeRulesError(Exception):
    """ An error occurred while applying rules to web scraping activities. """


class ScrapeSetError(Exception):
    """ An error occurred while managing the web scraping document set. """


@dataclass()
class ConfigDefaults:
    _debug: bool = False
    _log: bool = False and _debug
    _fuzzy: bool = True


def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error("Error during requests to {0} : {1}".format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers["Content-Type"].lower()
    return (
        resp.status_code == 200
        and content_type is not None
        and content_type.find("html") > -1
    )


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
def __tests__(args) -> int:
    """ Run Debug Tests for script if _debug_ = True. """

    print(f"{DEFAULT_PARSER=}")
    url = "https://realpython.com/blog/"
    raw_html = simple_get(url)
    html = soup(url)
    pprint(html)
    return 0


def __main__(args=argv[1:]) -> int:
    """ CLI script main entry point. """
    try:
        print("before")
        # raise WebPageError("test it")
        print("after")
    except:
        log_web.error()
        print("log")

    #! script testing
    if _debug_:
        __tests__(args)


if __name__ == "__main__":  # if script is loaded directly from CLI
    print("hello world")
    __main__()


""" Notes
    from tutorial ... moved out of __test__()

    raw_html = simple_get("https://realpython.com/blog/")
    print(len(raw_html))

    no_html = simple_get("https://realpython.com/blog/nope-not-gonna-find-it")

    print(no_html is None)

    # raw_html = open("contrived.html").read()
    """
