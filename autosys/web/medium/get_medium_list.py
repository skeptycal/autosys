#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import re
import requests

SET_DEBUG: bool = True
RE_document_article = '^\b*'
RE_pattern_document_article: re.Pattern = re.compile(
    RE_document_article, re.IGNORECASE)
FMT_URL_STATUSCODE_TEST = "url_test: GET request to {} returns {}"


def dbprint(*args, **kwargs):
    if SET_DEBUG:
        print(*args, **kwargs)


def safe_run(func):
    """ Decorator to handle errors in functions that often throw errors. Eliminates the need for multiple try/catch blocks.
    """
    def func_wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            dbprint(e)
            return None
    return func_wrapper


def url_test(url, fmt=FMT_URL_STATUSCODE_TEST) -> str:
    """ Return formatted response from <url>."""
    r = requests.get(url)
    return fmt.format(url, r.status_code)


@safe_run
def get(url) -> (str, int):  # type: ignore
    """ Return text of response from <url>. """
    r = requests.get(url)
    if r.status_code != 200:
        return r.status_code
    else:
        return requests.get(url).text


def get_article(url) -> str:
    try:
        r: requests.Response = requests.get(url)
    except requests.RequestException as e:
        dbprint(f"{e=}")
        raise
    dbprint(f"{r.status_code=}")
    return r.text
    # if r.status_code
    # pass


def main():
    '''
    CLI script main entry point.
    '''
    url = 'https://www.python.org'
    # dbprint(url_test(url))
    print(get('stuff'))

    med_list = [
        'https://medium.com/better-programming/stop-using-lists-for-everything-in-python-46fad15217f4',
        'https://medium.com/starts-with-a-bang/5-scientific-myths-you-probably-believe-about-the-universe-9a34597d7435',
    ]
    article_list = []
    for url in med_list:
        article_list.append(get_article(url))


if __name__ == "__main__":  # if script is loaded directly from CLI
    main()
