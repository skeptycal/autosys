import sys
import os
import mimetypes
from os import linesep as NL
from sys import stderr, stdout
from pathlib import Path
from wsgiref import simple_server, util

try:
    DEFAULT_ENCODING
except:
    from locale import getpreferredencoding
    DEFAULT_ENCODING: str = getpreferredencoding(do_setlocale=True) or "utf-8"


def get_html_template() -> (str):
    return """<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Learning the DOM</title>
    </head>

    <body>
        <h1>Document Object Model</h1>
        {}
    </body>
</html>
"""


def get_html_file() -> (str):
    template = get_html_template()
    body = ''
    body_list = []
    for f in Path().iterdir():
        body_list.append(str(f))
    body = NL.join(body_list)
    return template.format(body)


def create_index_file(file_name='index.html'):
    with open(file_name, mode='w') as fh:
        fh.write(get_html_file())


data = get_html_file()
print(data)
create_index_file()
