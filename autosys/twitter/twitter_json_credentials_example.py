#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Creates twitter credentials json file from user authentication data.

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

import json

# Enter your keys/secrets as strings in the following fields
credentials = {}
credentials["CONSUMER_KEY"] = "<put your information here>"
credentials["CONSUMER_SECRET"] = "<put your information here>"
credentials["ACCESS_TOKEN"] = "<put your information here>"
credentials["ACCESS_SECRET"] = "<put your information here>"

# Save the credentials object to file
with open("twitter_credentials_private.json", "w") as f:
    json.dump(credentials, f)
