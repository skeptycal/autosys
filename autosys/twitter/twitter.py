#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# !---------------------------------------------- Imports
if True:  # ! -- System Imports
    import requests
    import sys

if True:  # ! -- Specific System Imports
    from base64 import b64decode, b64encode
    from pathlib import Path
    from typing import Dict, List
    try:
        import ujson as json
    except:
        import json
if True:  # ! -- Package Imports
    from autosys.utils import dbprint, read, NL

#!---------------------------------------------- CONSTANTS
DEFAULT_BASE_URL: str = 'https://api.twitter.com/'
CWD: Path = Path(__file__).resolve().parents[0]
DEFAULT_TWITTER_CREDENTIAL_FILE: Path = CWD / "twitter_credentials_private.json"
_debug_: bool = True

#!---------------------------------------------- Utilities


def try_it(func):
    """ Wrapper to catch exceptions.

        func   - function wrapped by decorator @try_it

        Return - normal function return or Exception
        """
    def tried(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return e
    return tried(*args, **kwargs)


def GET(url='http://www.example.com'):
    return requests.get(url)


def api_test():
    url = "http://httpbin.org/post"

    payload = "{\n    \"key1\": 1,\n    \"key2\": \"value2\"\n}"
    headers = {
        'Content-Type': "application/json,text/plain",
        'User-Agent': "PostmanRuntime/7.15.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "e908a437-88ea-4b00-af53-7a9a49033830,ba90e008-0f7f-4576-beb8-b7739c8961f1",
        'Host': "httpbin.org",
        'accept-encoding': "gzip, deflate",
        'content-length': "42",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)

#!---------------------------------------------- encoding utilities


def encode64(s):
    """ Return ascii string encoded to Base64.

        utf-8 -> ascii -> base64 -> ascii """
    return b64encode(s.encode('ascii')).decode('ascii')


def decode64(s):
    """ Return ascii string decoded from Base64.

        utf-8 -> base64 -> ascii -> utf-8 """
    return b64decode(s.encode('ascii')).decode('ascii')


def binary_encode_64(binary_filename: str):
    """ Returns a base64 string from decoded binary file. """
    try:
        with open(binary_filename, 'rb') as binary_file:
            return b64encode(binary_file.read()).decode('utf-8')
    except OSError as e:
        return ''


def binary_decode_64(base64_img: str, binary_filename: str):
    """ Encodes a base64 string to bytes and writes it to a binary file. """
    try:
        base64_img_bytes = base64_img.encode('utf-8')
        with open(binary_filename, 'wb') as file_to_save:
            file_to_save.write(base64.decodebytes(base64_img_bytes))
        return 0  # 0 = success ...
    except OSError as e:
        return e


def print_binary(data):
    for byte in data:
        print(format(byte, '08b'), end=" ")

#!---------------------------------------------- Classes


class TwitterAPIError(Exception):
    """ Base Class for Twitter API Errors. """
    pass


class TwitterKeys():
    def __init__(self, filename=DEFAULT_TWITTER_CREDENTIAL_FILE):
        self._filename: Path = filename
        self._credentials: Dict[str, str] = {}
        self._load()

    def __str__(self):
        return self.encoded_key

    def _load(self):
        """ Get twitter credentials from file object. """
        self._credentials = {}
        self._encoded_key: Unicode = r''
        try:
            with open(self._filename, "r") as f:
                self._credentials = json.load(f)
        except Exception as e:
            raise TwitterAPIError(
                f"The credential file ({self._filename}) was not loaded.{NL}Error: {e}.")

    def save(self, credentials):
        """ Save the credentials dictionary object to a json file. """
        if isinstance(credentials, dict):
            self._credentials = credentials
            if self.check:
                with open(self._filename, "w") as f:
                    json.dump(credentials, f)
                self._load()  # ! read back file from disk to verify
                if not self.check:
                    raise TwitterAPIError(
                        f"The file did not load and verify correctly: {self._filename}")
                return 0
            raise TwitterAPIError(
                'The provided credentials are missing values.')
        raise TwitterAPIError(
            'The provided credentials are not in proper dictionary format.')

    @property
    def encoded_key(self):
        """ Create and store encoded key for request headers. """
        # ? should this be stored? cached? or created as needed each time?
        if not self._encoded_key:  # create key if needed
            self._encoded_key = encode64(f"{self.c_key}:{self.c_secret}")
        return self._encoded_key

 #!-------------------------------- TwitterKeys properties

    @property
    def check(self):
        """ Return 0 for good self-test, 1 otherwise. """
        return (self.c_key is None and self.c_secret is None and self.a_token is None and self.a_secret is None)

    @property
    def c_key(self):
        try:
            return self._credentials["CONSUMER_KEY"]
        except:
            return None

    @property
    def c_secret(self):
        try:
            return self._credentials["CONSUMER_SECRET"]
        except:
            return None

    @property
    def a_token(self):
        try:
            return self._credentials["ACCESS_TOKEN"]
        except:
            return None

    @property
    def a_secret(self):
        try:
            return self._credentials["ACCESS_SECRET"]
        except:
            return None


tk = TwitterKeys()


def twitter_credential_json_file_create():
    # Enter your keys/secrets as strings in the following fields
    credentials = {}
    credentials["CONSUMER_KEY"] = ""
    credentials["CONSUMER_SECRET"] = ""
    credentials["ACCESS_TOKEN"] = ""
    credentials["ACCESS_SECRET"] = ""
    tk_save = TwitterKeys()
    tk_save.save(credentials)
    del tk_save


class APIconnect():

    def __init__(self, base_url=DEFAULT_BASE_URL):
        pass
        # create url for API request:

    # dbprint(f"{base_url=}")
    # auth_url = '{}oauth2/token'.format(base_url)
    # dbprint(f"{auth_url=}")
    # dbprint()
    # auth_headers = {
    #     'Authorization': 'Basic {}'.format(tk),
    #     'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    # }
    # auth_data = {
    #     'grant_type': 'client_credentials'
    # }

    # auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
    # dbprint('Auth response: ', auth_resp.status_code)

    # return 0
#!---------------------------------------------- Script Tests


# __all__ = [
    # 'DEFAULT_BASE_URL',
    # 'DEFAULT_TWITTER_CREDENTIAL_FILE',
    # 'TwitterAPIError',
    # 'try_it',
    # 'TwitterKeys',
    # 'tk',
    # 'key_save',
    # 'APIconnect',
    # 'dbprint',
    # 'read'
    # ]


def _tests_(args):
    """ Run Debug Tests for script if _debug_ = True. """
    print(GET())
    # from autosys.utils import print_dict
    tk_tmp = TwitterKeys()
    print(f"{_debug_=}")
    # print(f"{DEFAULT_BASE_URL=}")
    # print(f"{DEFAULT_TWITTER_CREDENTIAL_FILE=}")

    print('Partial encoded key from class TwitterKeys: ')
    print(tk_tmp.encoded_key[1:5])
    tk_save
    # print_dict(globals())
    # api_test()


def _main_(args):
    """ CLI script main entry point. """
    #! script testing
    if _debug_:
        return _tests_(args)
    return 0


if __name__ == "__main__":  # if script is loaded directly from CLI
    global script_name
    script_name = sys.argv[0]
    _main_(sys.argv[1:])


""" Original long method before pulling it out to a utility function:

    @property
    def encoded_key(self):
        ''' Create encoded key for request headers. '''
        if not self._encoded_key:
            # Reformat the keys and encode them
            key_secret = f"{self.c_key}:{self.c_secret}".encode('ascii')
            # Transform from bytes to bytes that can be printed
            b64_encoded_key = b64encode(key_secret)
            # Transform from bytes back into Unicode
            self._encoded_key = b64_encoded_key.decode('ascii')
        return self._encoded_key

        """
