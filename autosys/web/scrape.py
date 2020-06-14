#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 'future imports'
from __future__ import absolute_import

# 'Standard Library'
import sys

from collections import deque
from contextlib import closing
from dataclasses import dataclass
from os import (
    environ as ENV,
    linesep as NL,
)
from pprint import pprint
from sys import (
    argv,
    stderr,
    stdout,
)

# 'package imports'
from autosys.web.web_basics import *
from bs4 import BeautifulSoup

# 'third party'
from requests import get
from requests.exceptions import RequestException

from typing import (
    Any,
    Deque,
    Dict,
    List,
    Tuple,
)

""" scrape.py - web scraping utilities for python
    (reference: https://realpython.com/python-web-scraping-practical-introduction/)

        copyright (c) 2019 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal
    """



try:
    import lxml as parser

    DEFAULT_PARSER = "lxml"
except:
    DEFAULT_PARSER = "html.parser"


# !---------------------------------------------- Custom Types


@dataclass(frozen=True)
class ScrapeRules(List[Any]):
    """ A list of functions, regex matches, or other checks to perform
        that keep the web scraper from doing anything unwanted. """

    triggers: List[Any] = []


@dataclass()
class WebDocument:
    """ Manages a List of additional url information for webpages.
        - Places the url in a data structure with additional optional fields
        - Allows automated recording of data during the web scraping process.
        - Any method that begins with '__wd_auto_' runs on url access
        - Add additional temporary methods with decorators
        - Add additional permanent methods with subclassing
        - Each method can be toggled on or off individually
        - Performance information for each addon is recorded
        - Gathers data that would otherwise be lost.
        - the input and output can remain a simple url.
        - each url may have multiple access and generate an audit trail

        Examples of optional fields. Add others by subclassing.
        - date and time of web access
        - author and contributor names and info
        - info required for citations
        - ping and download times
        - current user / machine / os / user-agent / environment
        - DNS server and proxy information
        - redirections encountered
        - additional unplanned data packets (is data encapsulated?)
        - complete status information (instead of just 200==success)
        - location of further resources (nonlocal links / images)
        - generate a list of further resources as a script
        """

    url: str


@dataclass
class ScrapeDocument(WebDocument):
    scrape_rules: List[Any] = []


@dataclass()
class ScrapeDocumentSet:
    url_list: List[str] = []
    config: ConfigDefaults = ConfigDefaults()
    DEFAULT_URL_HISTORY: int = 10000
    _url_set: Deque = deque(url_list, maxlen=DEFAULT_URL_HISTORY)
    optional_fields: List[Any] = WD_AUTO_STANDARD_FIELDS
    scrape_rules_list: List[Any] = DEFAULT_SCRAPE_RULES

    def __append__(self, url):
        self._url_set.__append__(
            ScrapeDocument(url=url, scrape_rules=self.scrape_rules_list))


# !---------------------------------------------- Script Tests
def __tests__(args) -> int:
    """ Run Debug Tests for script if _debug_ = True. """

    print(f"{DEFAULT_PARSER=}")
    url = "https://realpython.com/blog/"
    raw_html = simple_get(url)
    html = soup(url)
    pprint(html)
    return 0


def __main__(args) -> int:
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
