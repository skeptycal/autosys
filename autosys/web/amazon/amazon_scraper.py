#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" amazon_scraper.py

Usage:
  amazon_scraper.py <url> [-o=<file_name>] [--format=<json|csv|txt|html>] [--log=<True|False>]
  amazon_scraper.py <search_string> [-o=<file_name>] [--format=<json|csv|txt|html>] [--log=<True|False>]
  amazon_scraper.py [start|stop|config|test] <service_name> [--args=<args>] [--log=<True|False>]
  amazon_scraper.py (-h | --help)
  amazon_scraper.py --version

Options:
  --output=<file_name>              Output file     [default: url-based]
  --format=<json|csv|txt|html>      Output format   [default: json]
  --args=<args>                     Arguments passed to automation services
  --log=<True|False>                Log activity to file log
  -h --help                         Show this screen.
  --version                         Show version.

Scrape the Amazon.com website for specific data and log it in the specified
format. Automation services are also available.

******************************************************************************

 `AutoSys` package
        copyright (c) 2018 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`

"""

# 'Standard Library'
import sys
import threading
# builtins
import time

from dataclasses import dataclass
from datetime import datetime
from multiprocessing import Manager, Pool, Process, Queue

# 'package imports'
from autosys.text_utils.nowandthen import now

# 'third party'
import pandas as pd
# third party packages
import requests

from bs4 import BeautifulSoup

__author__ = "Michael Treanor"
__email__ = "skeptycal@gmail.com"
__version__ = "0.1.0"

# use proxies in requests so as to proxy your request via a proxy server
# as some sites may block the IP if traffic generated by an IP is too high
proxies = {
    "http": "http://134.119.205.253:8080",
    "https": "http://134.119.205.253:8080",
}
startTime = time.time()
qcount = 0
products = []  # List to store name of the product
prices = []  # List to store price of the product
ratings = []  # List to store ratings of the product
no_pages = 20


@dataclass
class Items:
    quantity: int
    name: str
    price: int
    rating: float


class ItemList(list):
    url: str
    query: str
    datetime: datetime = now()


def get_data(pageNo, q):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "DNT": "1",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1",
    }

    r = requests.get(
        "https://www.amazon.com/s?k=laptops&page=" + str(pageNo),
        headers=headers,
    )  # , proxies=proxies)
    content = r.content
    soup = BeautifulSoup(content)
    # print(soup.encode('utf-8')) # uncomment this in case there is some non UTF-8 character in the content and
    # you get error

    for d in soup.findAll(
        "div",
        attrs={
            "class": "sg-col-4-of-12 sg-col-8-of-16 sg-col-16-of-24 sg-col-12-of-20 sg-col-24-of-32 sg-col sg-col-28-of-36 sg-col-20-of-28"
        },
    ):
        name = d.find(
            "span", attrs={"class": "a-size-medium a-color-base a-text-normal"}
        )
        price = d.find("span", attrs={"class": "a-offscreen"})
        rating = d.find("span", attrs={"class": "a-icon-alt"})
        all = []

        if name is not None:
            all.append(name.text)
        else:
            all.append("unknown-product")

        if price is not None:
            all.append(price.text)
        else:
            all.append("$0")

        if rating is not None:
            all.append(rating.text)
        else:
            all.append("-1")
        q.put(all)
        # print("---------------------------------------------------------------")


results = []
if __name__ == "__main__":
    m = Manager()
    q = (
        m.Queue()
    )  # use this manager Queue instead of multiprocessing Queue as that causes error
    p = {}
    if sys.argv[1] in [
        "t",
        "p",
    ]:  # user decides which method to invoke: thread, process or pool
        for i in range(1, no_pages):
            if sys.argv[1] in ["t"]:
                print("starting thread: ", i)
                p[i] = threading.Thread(target=get_data, args=(i, q))
                p[i].start()
            elif sys.argv[1] in ["p"]:
                print("starting process: ", i)
                p[i] = Process(target=get_data, args=(i, q))
                p[i].start()
        # join should be done in seperate for loop
        # reason being that once we join within previous for loop, join for p1 will start working
        # and hence will not allow the code to run after one iteration till that join is complete, ie.
        # the thread which is started as p1 is completed, so it essentially becomes a serial work instead of
        # parallel
        for i in range(1, no_pages):
            p[i].join()
    else:
        pool_tuple = [(x, q) for x in range(1, no_pages)]
        with Pool(processes=8) as pool:
            print("in pool")
            results = pool.starmap(get_data, pool_tuple)

    while q.empty() is not True:
        qcount = qcount + 1
        queue_top = q.get()
        products.append(queue_top[0])
        prices.append(queue_top[1])
        ratings.append(queue_top[2])

    print(
        "total time taken: ", str(time.time() - startTime), " qcount: ", qcount
    )
    # print(q.get())
    df = pd.DataFrame(
        {"Product Name": products, "Price": prices, "Ratings": ratings}
    )
    print(df)
    df.to_csv("products.csv", index=False, encoding="utf-8")
