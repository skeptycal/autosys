#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" as_flask.py - basic Flask app
    Reference: https://stackoverflow.com/a/26853961
    ---
    Copyright (c) 2018 [Michael Treanor][2]

    AutoSys is licensed under the [MIT License][3]

    [1]: https://www.github.com/skeptycal/autosys
    [2]: https://www.twitter.com/skeptycal
    [3]: https://opensource.org/licenses/MIT
    """

if True:
    import flask
    from flask import current_app, request
    from random import random, choice, choices
    # from autosys.profiler.quicktime import QuickTime as qt

try:
    DEFAULT_ENCODING
except:
    from locale import getpreferredencoding
    DEFAULT_ENCODING: str = getpreferredencoding(do_setlocale=True) or "utf-8"

try:
    from ujson import dumps
    JSON_PARSER = "ujson"
except ImportError as e:
    from json import dumps
    JSON_PARSER = "json"


class FlaskJSONParameterError:
    "ultrajsonify behavior is undefined when passed both args and kwargs"


def ultrajsonify(*args, **kwargs):
    """This function reimplements ``flask.json.jsonify``
    using ``ujson.dumps`` instead of ``json.dumps``.
    """
    indent = 0
    ensure_ascii = current_app.config.get("JSON_AS_ASCII", True)
    mimetype = current_app.config.get("JSONIFY_MIMETYPE", "application/json")

    if (current_app.config["JSONIFY_PRETTYPRINT_REGULAR"]
            and not request.is_xhr):
        indent = 2

        # if (args and kwargs) or not(args and kwargs):
    if (args and kwargs):
        raise FlaskJSONParameterError

    data = args[0] if len(args) == 1 else args or kwargs

    return current_app.response_class(
        dumps(data, indent=indent, ensure_ascii=ensure_ascii),
        mimetype=mimetype,
    )


flask.json.jsonify = ultrajsonify


def random_binary(n=100, set_size=2):
    return [choices([0, 1], k=set_size) for _ in range(n)]


def random_binary_gen(n=10, set_size=2):
    yield (choices((0, 1), set_size) for _ in range(n))


def xor1(a, b):
    return bool(a) != bool(b)


def xor2(a, b):
    return bool(a) ^ bool(b)


def xor3(a, b):
    return (a + b) == 1


def xor4(*args):
    return any(args)


def xor5(*args, **kwargs):
    return (args and kwargs) or not(args and kwargs)


fake = []
fake = random_binary(n=100)

# print(fake)

for c in fake:
    a, b = c
    print(a, b)
    print(qt(xor1(a, b)))
    # timeit('xor1(a, b)')
