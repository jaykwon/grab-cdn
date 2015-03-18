import sys
import os

import requests
from bs4 import BeautifulSoup

import cdn


GOOGLE = "https://developers.google.com/speed/libraries/devguide"


def get_stylesheets(links):
    response = []
    for link in links:
        lines = link.text.split("<br>")
        for line in lines:
            if line.startswith("<link"):
                response.append(line.split("\"")[3])
    return response


def get_javascript(links):
    response = []
    for link in links:
        try:
            url = link.text.split("\"")[1]
            if url.startswith('http'):
                response.append(url)
        except IndexError:
            pass
    return response


def get_urls():
    r = requests.get(GOOGLE)
    soup = BeautifulSoup(r.text)
    links = soup.find_all('code')
    return get_javascript(links) + get_stylesheets(links)


if __name__ == '__main__':
    links = get_urls()
    for link in links:
        cdn.download_link(link, 'google')
