#!/usr/bin/env python3
'''
Small wsgiref based web server. Takes a path to serve from and an
optional port number (defaults to 8000), then tries to serve files.
Mime types are guessed from the file names, 404 errors are raised
if the file is not found. Used for the make serve target in Doc.
'''
import sys
import os
import mimetypes
from os import linesep as NL
from sys import stderr, stdout, path as PYTHONPATH
from pathlib import Path

here = Path(__file__).resolve().parent
parents = Path(__file__).resolve().parents

for parent in parents:
    if Path(parent/'README.md').exists():
        break
    if parent not in PYTHONPATH:
        print(parent)
        PYTHONPATH.insert(0, parent)

if here not in PYTHONPATH:
    PYTHONPATH.insert(0, here)

while True:
    try:
        continue
    except KeyboardInterrupt:
        break

if True:
    from wsgiref import simple_server, util

    import autosys.web.webpages.make_html_index

try:
    DEFAULT_ENCODING
except:
    from locale import getpreferredencoding
    DEFAULT_ENCODING: str = getpreferredencoding(do_setlocale=True) or "utf-8"


def app(environ, respond):
    fn = os.path.join(path, environ['PATH_INFO'][1:])
    if '.' not in fn.split(os.path.sep)[-1]:
        fn = os.path.join(fn, 'index.html')
    type = mimetypes.guess_type(fn)[0]

    if os.path.exists(fn):
        respond('200 OK', [('Content-Type', type)])
        return util.FileWrapper(open(fn, "rb"))
    else:
        respond('404 Not Found', [('Content-Type', 'text/plain')])
        return [b'not found']


if __name__ == '__main__':
    makehtmlindex()
    # print(f"{get_html_file()}")
    pass
if True:
    path = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 8000
    httpd = simple_server.make_server('', port, app)
    print("Serving {} on port {}, control-C to stop".format(path, port))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down.")
        httpd.server_close()
