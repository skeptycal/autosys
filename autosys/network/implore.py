#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" implore.py - An even more desperate way to make requests for Humans.™ """
""" GOALS:
    By creating this app, I wanted to answer these questions:

    - What are the internet activities that I use or want most often?
    - What are the things that are feasible, but that I cannot easily do?

    Here is a list of items I came up with. I have solved them to some degree, but any advice or suggestions is welcome. See Contributors document for information.

    - Get a webpage
    - Modify CSS
    - Convert to a 3d object
        - front is main page
        - shape / depth controlled by varying functions
    - Collect links, images, tags, or something else from webpages
    - Create a 'map' of link destinations
    - Create an image catalog for a specific site(with CSS)
    - Interact with underlying database
    - Disable certain JS apps
    - Disable or interact with certain trackers
    - Watch for cookies and other local data / permissions
    - Block specific activities of specific sites
    - Search for English (or language) words and separate them from tags
    - Analyze metadata
    - Count types of tags and metadata
    - Analyze or avoid ads
    - Test for API functionality
    """


if True:  # Standard Library Dependencies
    from collections import Counter, deque
    from datetime import datetime
    from pprint import pprint
    from time import time, sleep, process_time, perf_counter, gmtime, localtime
    from typing import Any, Dict, List, MutableSequence
    import cgitb
    import os
    import sys
    import traceback

SET_DEBUG: bool = True  # turn on for Dev Debugging
if SET_DEBUG:  # enable detailed logging
    # cgitb.enable([display[, logdir[, context[, format]]]])
    DEFAULT_CGITB_DISPLAY: int = 1  # 0 to suppress messages
    DEFAULT_CGITB_FILE_LOGDIR: str = os.path.join(os.path.dirname(__file__), 'LOGS')
    DEFAULT_CGITB_CONTEXT: int = 3  # 5 is the normal default
    DEFAULT_CGITB_FORMAT: str = 'html'

    cgitb.enable(logdir=DEFAULT_CGITB_FILE_LOGDIR,
                 display=DEFAULT_CGITB_DISPLAY,
                 context=DEFAULT_CGITB_CONTEXT,
                 format=DEFAULT_CGITB_FORMAT,
                 )

    DEFAULT_CGITB_ERROR: sys.exc_info = ()

if True:  # External Dependencies
    from apscheduler.schedulers.blocking import BlockingScheduler
    from bs4 import BeautifulSoup
    import requests
    try:
        import ujson as json  # faster json if available
    except:
        import json

if True:  # setup html parser
    DEFAULT_PARSER: str = ''
    XML: bool = False  # whether XML parsing is available at all
    try:  # use <lxml> for speed (HTML and / or XML) (VERY fast)
        import lxml as parser
        DEFAULT_PARSER = 'lxml'
        XML = True
        XML_PARSER: str = 'xml'
    except:
        try:  # use <html5lib> for accuracy (VERY slow)
            import html5lib as parser
            DEFAULT_PARSER = 'html5lib'
        except:  # use <html5lib> Python's built-in html parser
            import html.parser as parser
            DEFAULT_PARSER = 'html.parser'

if True:  # Default constants
    # * time zones and scheduling
    USE_TZ: bool = False
    sch = BlockingScheduler()

    # * html and parsing
    DEFAULT_ENCODING: str = 'UTF-8'
    url: str = ''
    script_text: str = ''
    current_number: str

    now: struct_time = gmtime()


def db_print(*args, file=sys.stderr, **kwargs):
    """ Print messages to STDERR in debug mode (if <SET_DEBUG> is set) """
    if SET_DEBUG:
        print('@db ->', *args, **kwargs)


# contact_list.save_to_file() # with open('list.txt') as p: # p = json.load(p) # print(p)


@app.route("/")
def index():
    pass


def main_test():
    url = 'https://www.indeed.com/jobs?q=python&l=Remote'
    matches = soup_match(url, tag_name='div', attrs_pass={'class': 'title'})
    # for jobTitle in matches: # if "Developer" in jobTitle.text:
    # text(default_cell_number, 'jobTitle.text')  # break # elif "Jr" in jobTitle.text:
    # print(type(matches)) for match in matches: print(match.text.strip())
    # text(default_cell_number, 'jobTitle.text')  # break


def main():
    db_print(f"{DEFAULT_PARSER}")
    wps = WebPageSet([], check_links=True, maxlen=100)
    wps.append(WebPage('https://www.google.com'))
    wps.append(WebPage('fake page'))
    wps.append('fake page')


if __name__ == "__main__":
    cgitb.enable()
    db_print(cgitb.grey('test grey font'))
    try:
        app.run()
    except:
        pass

    # start_response('200 OK', [('Content-Type', 'text/html')])
    main()


# References
""" Choice of parser

    I use BeautifulSoup to work with html documents.

        Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours or days of work.

        https://www.crummy.com/software/BeautifulSoup/bs4/doc/

    According to the documentation:

        $ pip install lxml
        $ pip install html5lib

    do not use python's built in html parser (before python 3.2.2).

    - "lxml" - Use for speed (HTML)
    - "xml" - Use for speed (XML)
    - "html5lib" - Best accuracy ... very slow! (HTML)
    - "html.parser" - built in parser ... eh, it works (HTML)
    - lxml is also the ONLY supported XML parser


Latex / Bibtex

    - http://www.bibtex.org/
    - https://libguides.bates.edu/thesis_writers

Shields

    - https://shields.io/
    - https://simpleicons.org/?q=dj
    - https://docs.readthedocs.io/en/stable/badges.html
    - https://img.shields.io/badge/Django-v3-%23092E20?logo=django&color=#339933


    """
