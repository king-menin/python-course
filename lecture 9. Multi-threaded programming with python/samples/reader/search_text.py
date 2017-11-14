# -*- coding: utf-8 -*-
from requests import get
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import argparse
import codecs


def search_text(args, cons=False):
    tmp, query = args
    if cons:
        print(query)
    url = tmp.format(urlencode({"search": query}))
    req = get(url)
    assert req.status_code == 200, "request failed"
    soup = BeautifulSoup(req.text, "lxml")
    return " ".join(list(map(lambda x: str(x.text).replace("\n", " ").strip(),
                             soup.find("div", {'id': 'mw-content-text'}).findAll("p")[2:])))


def thread_job_multi_proc(args):
    tmp, query = args
    return query, search_text((tmp, query))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("tmp", type=str)
    parser.add_argument("query")
    args = parser.parse_args()
    print(codecs.encode(search_text((args.tmp, args.query), True), encoding="utf-8", errors="ignore"))
