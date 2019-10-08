#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""
import importlib
import sys
from timeit import timeit
from typing import List


def json1():
    import json


def json2():
    import ujson


def json3():
    import rapidjson


def json4():
    import ujson_x


def json5():
    import nujson


# def json6():
#     import autosys_json


if __name__ == "__main__":
    json_import_list: List[str] = ['simplejson', 'json', 'ujson', 'ujson-x', ]
    for json_import in json_import_list:
        try:
            importlib.
            import json_import as json
        except ImportError as e:
            print(e)
            continue


# module replacements
# Reference: https://pypi.org/project/speed-stack/#files
def _replace(replacement: str, target: str) -> bool:
    try:
        import sys
        if target in sys.modules:
            del sys.modules[target]
        sys.modules[target] = __import__(replacement)
        return True
    except:
        return False


def _hook():
    try:
        import uvloop
        import asyncio
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    except:
        pass

    if not _replace("ujson", "json"):
        _replace("rapidjson", "json")
    _replace("dill", "pickle")
    _replace("multiprocess", "multiprocessing")


try:
    _hook()
except:
    pass
