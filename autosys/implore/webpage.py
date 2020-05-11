# -*- coding: utf-8 -*-
""" Part of the `AutoSys` package
        copyright (c) 2019 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """
__license__ = "MIT"


class WebPageError(TypeError):
    """  # Exception raised for errors in the WebPage class. """
    pass


class WebPage(requests.Response):
    """ A local representation of a webpage. This object is able to analyze itself, share data, and perform its duties unsupervised.

    parameters

    url: the source of the original page grab. Use the <refresh> command to get an updated version."""
    # >>> r = requests.get('https://api.github.com/user',

    def __init__(self, url):
        super().__init__()
        self.url: str = url
        self.dirty: bool = True
        self.last_status: int = 0
        self.timestamp: struct_time = gmtime()
        # self.tags = {}
        # self.auth: Tuple[str, str] = ('user', 'pass')
        # auth = ('user', 'pass')

    def get_url_content(self, url: str) -> str:
        """ Return decoded contents from <url> using default parameters. """
        self = requests.get(url)
        self.history.append()
        self.last_status = self.status_code
        if self.last_status == 200:
            return self.text
        else:
            return ''

    def tag_find(self, tag_name: str, attrs_pass: Dict[Any, Any], parser_pass: str = DEFAULT_PARSER) -> List[Any]:
        """ Find matching tags from url. """
        soup = BeautifulSoup(self.text, features=DEFAULT_PARSER)
        return soup.findAll(name=tag_name, attrs=attrs_pass)

    def tag_list(self, tag_name: str):
        if self.dirty:
            self.tags = Counter(self.text)
            return self.tags

    def to_markdown(self): pass

    def to_json(self): return json.dumps(self.text)

    def stats(self): pass

    def soup(self): pass  # return BeautifulSoup()


class WebPageSet(deque):
    """ Stores and maintains a set of web pages. """
    DEFAULT_WEBPAGESET_SIZE = 2000  # maximum number of pages
    # TODO this should be 'maximum size' ... not count
    # ... and class should check it's own size

    def __init__(self, iterable: MutableSequence, maxlen: int = 0, check_links: bool = True, image_storage: str = ''):
        if not maxlen or maxlen < 1:
            maxlen = DEFAULT_WEBPAGESET_SIZE
        self.check_links = check_links
        self.store = True if image_storage else False
        self.image_storage = image_storage
        super().__init__(iterable, maxlen)

    def count(self):
        """ count tags, emails, ... whatever from the entire set """
        pass

    def common(self):
        """ find items that this pageset has in common. """
        pass

    def append(self, x):
        if isinstance(x, WebPage):
            super().append(x)
        else:
            if SET_DEBUG:
                db_print()
            else:
                raise (WebPageError)

    def size_check(self): print(self.__sizeof__())
