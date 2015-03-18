import sys
import os

import requests
from bs4 import BeautifulSoup

import cdn


MICROSOFT = "http://www.asp.net/ajax/cdn"


def get_urls():
    r = requests.get(MICROSOFT)
    soup = BeautifulSoup(r.text)
    links = soup.find_all('li')
    return [link.text for link in links if link.text.startswith('http')]


def get_vendor(link):
    return link.split('/')[4]


if __name__ == '__main__':
    base = 'libs'
    for link in get_urls():
        cdn.download_link(link, os.path.join(base, 'ajax-cdn', get_vendor(link)))
