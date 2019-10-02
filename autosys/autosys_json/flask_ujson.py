# -*- coding: utf-8 -*-
from flask import current_app, request
from ujson import dumps


def ultrajsonify(*args, **kwargs):
    """This function reimplements ``flask.json.jsonify``
    using ``ujson.dumps`` instead of ``json.dumps``.
    """
    indent = 0
    ensure_ascii = current_app.config.get("JSON_AS_ASCII", True)
    mimetype = current_app.config.get("JSONIFY_MIMETYPE", "application/json")

    if current_app.config["JSONIFY_PRETTYPRINT_REGULAR"] and not request.is_xhr:
        indent = 2

    if args and kwargs:
        raise ValueError(
            "ultrajsonify behavior undefined when passed both args and kwargs"
        )
    elif len(args) == 1:
        data = args[0]
    else:
        data = args or kwargs

    return current_app.response_class(
        dumps(data, indent=indent, ensure_ascii=ensure_ascii), mimetype=mimetype
    )
