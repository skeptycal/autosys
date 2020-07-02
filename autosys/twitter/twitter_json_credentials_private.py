#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Creates twitter credentials json file from user authentication data.

    #! Keep this file *PRIVATE* and do not submit it to source control!

    Keys and info can be obtained from the twitter developer site:
    https://developer.twitter.com/en (English Version, others available)

    ------------------------------------------------------------------------------

    MIT License
    Copyright (c) 2018 - 2020 Michael Treanor <https://www.skeptycal.com>

        Permission is hereby granted, free of charge, to any person obtaining a copy of
        this software and associated documentation files (the "Software"), to deal in
        the Software without restriction, including without limitation the rights to
        use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
        the Software, and to permit persons to whom the Software is furnished to do so,
        subject to the following conditions:

        The above copyright notice and this permission notice shall be included in all
        copies or substantial portions of the Software.

        THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
        IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
        FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
        COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
        IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
        CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
        """

# 'Standard Library'
from pathlib import Path
from sys import argv

try:
    import ujson as json
except:
    import json

here = Path(__file__).resolve()
print(here)
TWITTER_CREDENTIALS_FILE_PRIVATE: str = "twitter_credentials_private.json"


# Enter your keys/secrets as strings in the following fields
credentials = {}
credentials["CONSUMER_KEY"] = "NMSAhbzNgr8EK8LboCoMnYSiO"
credentials[
    "CONSUMER_SECRET"
] = "ea92hIoBo0oW0NibgIgLiiSuVgYRjjBWnAM1S6CsJI6KOH8bYg"
credentials[
    "ACCESS_TOKEN"
] = "1439301-HlmicZvMEsNm64mrVzEkVMjBcWPvsEsyWLdv5Bw1B1"
credentials["ACCESS_SECRET"] = "mFf4mZcIV5aMka5l2vdJ9N61prHgKjQlc9yckIsKd1ywb"


def main(args=argv[1:]):
    fh_mode: str = ""
    filename: str = args[0] or TWITTER_CREDENTIALS_FILE_PRIVATE
    filename = filename.lower()

    if "private" not in filename:
        print("The word 'private' must appear in the filename.")
        print(f"The filename provided was {filename}.")
        return 1
    else:
        if Path(filename).exists():
            print(f"The filename {filename} exists and is being used.")
            fh_mode = "w"
        else:
            print(
                f"The filename {filename} does not exists and is being created."
            )
            fh_mode = "x"
        # Save the credentials object to file
        with open(TWITTER_CREDENTIALS_FILE_PRIVATE, fh_mode) as fh:
            json.dump(credentials, fh)
        return 0


if __name__ == "__main__":
    """ Write twitter credentials to file. """
    main()
