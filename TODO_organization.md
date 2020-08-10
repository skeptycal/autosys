## Autosys - common utilities for all projects

### default imports

```py
from os import linesep as NL, sep as PATHSEP, environ as ENV
from pathlib import Path
from pprint import pformat
from sys import argv, stdout, stderr, path as PYTHON_PATH
from typing import Any, Dict, List, Tuple
```

### version

-   \_get_copyright_date
-   meta_data

### utilities

-   setup
-   protected_exec ... from 'remove_lines.py'
-   limited_exec ...
-   list with join, etc features
-   fix_parens (with FIND_PARENS regex)
-   hash ... md5 ... salt
-   make file headers on \*.py, etc
-   lister
-   class Now - for common datetime stuff
-   strings - encode64, decode64
-   files - binary_encode_64, binary_decode_64
-   pretty print binary info

### strings and text

-   br
-   join
-   hr
-   argstr
-   s80 (80 column string)
-   vprint (variable print)
-   remove_lines
-   remove_inplace
-   display_markdown (etc)
-   isutf8
-   replace_all
-   rep_whitelist
-   fstring formatting (NpAlign, etc)

### decorators

-   time_it
-   log_it
-   try_it
-   profileit
-   dis_it
-   memoize_it
-   ram_it (memory usage)
-   gen_it (create generator)
-   lrucache
-   choose_feature (based on environment)
    e.g. v for verbose_on / verbose_off

### classes

-   Queue
-   BetterList
-   BetterDict
-   Singleton
-   str...

### setup

```py
from setuptools import setup, find_packages
from _version import *
```

-   def readme
-   class SetupAttrs
-   make .editorconfig
-   .env (PYTHONPATH=./venv/bin/python3)
-   .travis.yml
-   CHANGES.rst
-   CODE_OF_CONDUCT.md
-   CODING_STANDARDS.md
-   Dockerfile
-   .editorconfig
-   .eslintrc
-   .gitignore
-   .npmrc
-   .prettierignore
-   .prettierrc.js
-   .prettierrc.ES6.js
-   .sonarcloud.properties
-   .vscodeignore
-   defaults.py (default repo values)
-   LICENSE
-   MANIFEST.in (no longer needed)
-   README.md
-   README.rst
-   setup.cfg
-   setup.py (automated creation?)
-   TODO.md (repo goals)
-   tox.ini
-   tox

### Docs

-   \_config.yml (theme: jekyll-theme-minimal)
-   github.css
-   README.md

### config

```py
_debug_:bool = False # dev mode toggle
_log_:bool = _debug and False # _debug must be True
```

-   IS_64BITS

### CLI

-   `__init__.py` terminal setup
    -   IS_TTY, etc
    -   SUPPORTS_COLOR, etc
    -   minimal colors
-   AppDirs
-   AsciiChars
-   replace_all (needle/haystack)
-   replace with whitelist
-   make_safe_id (isidentifier())
-   class Terminal
-   class BasicColors
-   class LogColors
-   class AnAnsi
-   class CliArgs (docopts)
-   str class replacement
-   colors (css4, base, tableau, xkcd)
-   year
-   date
-   class Code8
-   class Code16
-   class Effects
-   class Ansi(str)
-   class ColorToggle
-   class NpChart
-   np_row
-   np_array usage for terminal colors ...

### File System

-   database to contain files
-   memory mapped to 'the FAT'
-   replace paths with search parameters and unique names (ids)
-   files can be grouped in any way
-   filter, sort, map, any list of files
-   file objects contain their disk location, but it is wrapped up and unused

### Parsers

-   change files to colorful, formatted output
-   for CLI or web
-   github has the web ones
-   there is an ANSI parser/formatter available222
-   pythontidy

### DashBoard

-   DashBoard class (Flask based)

### Web

-   Get (wrapper for requests)
-   class ApiSpy
-   Automate data collection (look for stuff that looks like data ...)
-   log_urls

### twitter

-   Get my account info
-   Search and report
-   create charts
-   add / delete followers
-   automate tweets on by push or by calendar
-   class TweetIt ... IttyTwitty
-   class TwitterKeys
-   twitter_credential_json_file_create
-   class APIConnect

### google

-   search and refine
-   specify types of sources allowed (educational, reputable, political, etc)
-   store in np_array
-   simple_get
-   is_good_response
-   get_p_tags
-   get_tags
-   soup
-   able to do this:

````py
from google_it import Google

my_list: List[str]: =[
    'www.skeptycal.com/about',
    'www.xxxxx.xxx',
    'www.example.com/data'
]

g = Google()
result = g.get_list(my_list)
result.research() # analyze topics / trustworthiness / etc
result.stats() # get stats: words / grammar / links / SEO quality / similar content
result.summarize() # create a summary (abstract)
result.results() # display known info (so far) in a dashboard style browser display
result.export() # save data to database / file
result.reset() # start over
print(result.google('What is the weather today in Barcelona?')) # grab the first link or google special info
result.import_it() # grab a dataset
result.merge_it() # merge current with new dataset, including finding similar columns of data to perform
result.structure() # setup virtual tables, relationships (OtM, OtO, MtM), rows, columns,primary keys, etc
result.profile() # try various formats of relationships and tables to get the most performance given a sample of the most common SQL queries (ML process?)
result.CRUD() # access data using SQL to CRUD



```

### medium

-   def get_article(url) -> str:
-   check links
-   parse stories
-   reformat to <MD, txt, doc, pdf, etc>
-   which text format is fastest to parse for NLP?
-   database? csv? json? txt?
-   `import counter` for basic data
-   use NLP
-   create summaries
-   research topics
-   locate related images (by license? size?)

### threading, execution control

-   Threading class
-   async / await

### Debug

-   `_log_` flag
-   log = Logger(`__file__`)
-   Logger class with
    -   variable reporting
    -   html generation
    -   dashboard streaming
-   verbosity flag
-   log flag
-   db_column ruler
-   argstr (again ...)
-   dbprint -> change to log.info
-   ErrC (C style error codes)
-   Custom Error classes
-   info, warning, error, exception
-   showstack
-   traceback

### profiling

-   time_it
-   class Benchmark
-   fibs tester
-   database tester
-   json tester
-   decorator for profiling (add function to database while it is being timed)

### `.gitignore` file

-   (download based on project)
-   use github repo and pass args ...

### `.ignore` file

```py
from os import getcwd

CWD = getcwd()

def _create_ignore_file(path: Path = CWD):
with open('.ignore',w) as file:
    file.write('\n'.join([
        "**/*/__pycache__/",
        "**/*/.mypy_cache/",
        "**/*/.pytest_cache/",
        "**/*/.vscode/",
        "**/*/*egg-info/",
        "**/*/node_modules/",
        "**/*/venv",
    ])
````
