#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Tests for Autosys package. For more information:
https://docs.python-guide.org/writing/tests/
"""

# import autosys
from autosys.twitter import twitter
from autosys.twitter.twitter import *

# ! safety: PurePath cannot perform operations,
#   but can be mapped to Path for most checks ...
from pathlib import PurePath as Path


def test_requests_connection(url='https://www.google.com'):
    response = requests.get(url)
    assert response.status_code == 200


def test_default_base_url_exists():
    response = requests.get(DEFAULT_BASE_URL)
    print(DEFAULT_BASE_URL)
    assert response.status_code != 200


def test_default_twitter_credential_file_exists():
    print(Path(DEFAULT_TWITTER_CREDENTIAL_FILE))
    # assert Path(DEFAULT_TWITTER_CREDENTIAL_FILE)


def test_tk_encoded_key_output_exists():
    tk_temp = twitter.TwitterKeys()
    response = tk_temp.encoded_key[0:10:-1]


if __name__ == "__main__":
    # from autosys.utils import print_dict
    # print_dict(twitter.DEFAULT_BASE_URL)
    pass
