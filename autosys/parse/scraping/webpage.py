#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" webpage - a class <WebPage> that represents a document and . It is designed for online documents that will be downloaded upon demand rather than stored in a database, but a database option is available for local implementation.

    Part of the `AutoSys` package
        copyright (c) 2019 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """
__license__ = "MIT"

# !------------------------------------- Imports
if True:  # standard library imports
    import re
    import sys

if True:  # standard library specifics
    from collections import deque
    from contextlib import closing
    from datetime import datetime
    from io import TextIOWrapper
    from sys import argv
    from time import perf_counter_ns as _timer
    from typing import (
        Any,
        Generator,
        List,
        Sequence,
        Dict,
        MutableSequence,
        Tuple,
    )

if True:  # outside requirements
    from requests import get
    from requests import Response
    from requests.exceptions import RequestException
    from bs4 import BeautifulSoup
    from bs4.element import ResultSet


DEFAULT_PARSER = "lxml"
DEFAULT_ENCODING = "utf-8"


class WebPageError(TypeError):
    """  # Exception raised for errors in the WebPage class. """

    pass


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


def simple_get(url):
    """ Attempts to get the content at `url` by making an HTTP GET request.
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


class WebPage:
    """ A local representation of a webpage. This object is able to analyze
        itself, share data, and perform its duties unsupervised.

        parameters

        url: the source of the original page. Use the <refresh> command to get
        an updated version.
        """

    # >>> r = requests.get('https://api.github.com/user',
    import requests

    def __init__(self, url: str):
        self.url = url
        self.resp = requests.get(url)
        self.last_status: int = 0
        self._timestamp: datetime = datetime.now()
        # self.tags = {}
        # self.auth: Tuple[str, str] = ('user', 'pass')
        # auth = ('user', 'pass')
        super().__init__()

    def __iter__(self):
        return self.tags

    def __next__(self):
        try:
            yield (t for t in self.soup.find_all())
        except:
            raise StopIteration

        # if self.n <= self.max:
        # result = 2 ** self.n
        # self.n += 1
        #     return result
        # else:
        #     raise StopIteration

    # ------------------------------------------ properties
    @property
    def soup(self):
        # return BeautifulSoup()
        return BeautifulSoup(self.text, features=DEFAULT_PARSER)

    @property
    def tags(self) -> ResultSet:
        try:
            yield (t for t in self.soup.find_all())
        except:
            yield []

    @property
    def links(self):
        yield (t for t in self.soup.findAll("a", href=True))

    @property
    def images(self):
        yield (t for t in self.soup.findAll("img"))

    @property
    def text(self) -> str:
        return self.resp.text if self.resp.text else ""

    @property
    def status(self) -> int:
        return self.resp.status_code if self.resp.status_code else -1

    @property
    def timestamp(self) -> str:
        try:
            return datetime.fromtimestamp(self._timestamp).isoformat()
        except:
            return ""

    # ------------------------------------------ properties

    def get_url_content(self, url: str) -> str:
        """ Return decoded contents from <url> using default parameters. """
        self = requests.get(url)
        self.history.append()
        self.last_status = self.status_code
        if self.last_status == 200:
            return self.text
        else:
            return ""

    def tag_find(
        self,
        tag_name: str,
        attrs_pass: Dict,
        parser_pass: str = DEFAULT_PARSER,
    ) -> List:
        """ Find matching tags from url. """
        return self.soup.findAll(name=tag_name, attrs=attrs_pass)

    def tag_list(self, tag_name: str):
        if self.dirty:
            self.tags = Counter(self.text)
            return self.tags

    def to_markdown(self):
        pass

    def to_json(self):
        return json.dumps(self.text)

    def stats(self):
        pass

    def tags(
        self,
        name=None,
        attrs={},
        recursive=True,
        text=None,
        limit=None,
        **kwargs,
    ):
        return self.soup.findAll(
            name=name,
            attrs=attrs,
            recursive=recursive,
            text=text,
            limit=limit,
            **kwargs,
        )

    def __str__(self):
        return self.resp.url if self.resp.url else ""

    def __repr__(self):
        return f"response = {self.resp.status_code} for {len(self.resp.content)} bytes from {self.url}."

    def log_error(self, e: RequestException):
        """
            It is always a good idea to log errors.
            This function just prints them, but you can
            make it do anything.
            """
        print(e, file=sys.stderr)

    def is_valid(self, r: Response = None) -> bool:
        """ Return true if an HTTP response status is 200.

            The default response is <self.resp>.
            """
        if not r:
            r = self.resp
        return r.status_code == 200

    def is_html(self, r: Response = None) -> bool:
        """ Returns True if an HTTP response 'seems' to be HTML, False otherwise.

            The default response is <self>. Use parameter to test other urls.
            """
        if not r:
            r = self
        try:
            requests.Response.headers
            content_type = r.headers["Content-Type"].lower()
            return (
                r.status_code == 200
                and content_type is not None
                and content_type.find("html") > -1
            )
        except:
            return False

    # @time_it
    def _get(self, url: str = "", html: bool = True) -> (Response, Exception):
        """ Return the response an HTTP GET request to url.

            The default url is <self.url>, but outside url's can be tested as needed by setting <url>.

            If <html> is True, test the content-type of the response is some kind of HTML/XML and return the response, otherwise return None. (This is the default.)
            """
        # TODO check for dirty, refresh time, cookie, etc

        if not url:
            url = self.url
        try:
            with _closing(_get(url, stream=True)) as r:
                if self.is_valid(r):
                    if html:
                        if self.is_html(r):
                            return r
                    else:
                        return r
                else:
                    return None

        except RequestException as e:
            log_error(
                "Error during requests to {0} : {1}".format(self.url, str(e))
            )
            return None


class WebPageDeque(deque):
    """ Stores and maintains a set of web pages. """

    DEFAULT_WEBPAGESET_SIZE = 2000  # maximum number of pages
    # TODO this should be 'maximum size' ... not count
    # ... and class should check it's own size

    def __init__(
        self,
        iterable: MutableSequence,
        maxlen: int = 0,
        check_links: bool = True,
        image_storage: str = "",
    ):
        if maxlen < 1:
            maxlen = DEFAULT_WEBPAGESET_SIZE
        self.maxlen = maxlen
        self.check_links = check_links
        self.store = True if image_storage else False
        self.image_storage = image_storage
        super().__init__(iterable, maxlen)

    def count(self, needle=r"<a.*>"):
        """ count tags, emails, ... whatever from the entire set """
        pass

    def common(self):
        """ find items that this pageset has in common. """
        pass

    def append(self, x):
        """ Only append WebPage instances. """
        if isinstance(x, WebPage):
            super().append(x)
        else:
            if SET_DEBUG:
                db_print()
            else:
                raise (WebPageError)

    def size_check(self):
        print(self.__sizeof__())


sample_urls = [
    "http://foo.com/blah_blah",
    "http://foo.com/blah_blah/",
    "(Something like http://foo.com/blah_blah)",
    "http://foo.com/blah_blah_(wikipedia)",
    "(Something like http://foo.com/blah_blah_(wikipedia))",
    "http://foo.com/blah_blah.",
    "http://foo.com/blah_blah/.",
    "<http://foo.com/blah_blah>",
    "<http://foo.com/blah_blah/>",
    "http://foo.com/blah_blah,",
    "http://www.example.com/wpstyle/?p=364.",
    "http://✪df.ws/123",
    "rdar://1234",
    "rdar:/1234",
    "http://userid:password@example.com:8080",
    "http://userid@example.com",
    "http://userid@example.com:8080",
    "http://userid:password@example.com",
    "http://example.com:8080 x-yojimbo-item://6303E4C1-xxxx-45A6-AB9D-3A908F59AE0E",
    "message://%3c330e7f8409726r6a4ba78dkf1fd71420c1bf6ff@mail.gmail.com%3e",
    "http://➡.ws/䨹",
    "www.➡.ws/䨹",
    "<tag>http://example.com</tag>",
    "Just a www.example.com link.",
]

RE_STR_URL_MATCH = r'(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))'
RE_PATTERN_URL_MATCH = re.compile(RE_STR_URL_MATCH)


def re_matches(s, pat=RE_PATTERN_URL_MATCH):
    """ Return True if s matches pattern.
        Default is url pattern.
        """
    return re.match(pat, s)


def is_url(url) -> bool:
    """ regex url match
        https://daringfireball.net/2009/11/liberal_regex_for_matching_urls
        initial pattern:
        \b(([\w-]+://?|www[.])[^\s()<>]+(?:\([\w\d]+\)|([^[:punct:]\s]|/)))
        superseded to:
        https://daringfireball.net/2010/07/improved_regex_for_matching_urls
        """
    return re_matches(url, RE_PATTERN_URL_MATCH)


def _test_(url):
    w = WebPage(url)
    r = w.status
    print(w)
    print(r)
    print(w.is_html(r))
    print()

    print(w)
    # content_type = w.headers['Content-Type'].lower()
    # print(content_type)
    # print(w.resp.headers['Content-Type'].lower())


def _main_():
    """
    CLI script main entry point.
    """
    url = "https://realpython.com/blog/"

    _test_(url)

    print(simple_get(url=url))

    w = WebPage("https://realpython.com/blog/")

    print(w.text)

    url = "https://realpython.com/blog/nope-not-gonna-find-it"

    print(WebPage(url))


if __name__ == "__main__":  # if script is loaded directly from CLI
    _main_()
