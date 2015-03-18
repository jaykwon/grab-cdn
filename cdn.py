import os

import requests

import google
import ajax


def download_link(link, destination="."):
    if not os.path.exists(destination):
        os.makedirs(destination)
    name = os.path.basename(link)
    output = os.path.join(destination, name)
    with open(output, 'wb') as handle:
        response = requests.get(link, stream=True)
        print destination, response.status_code
        if not response.ok:
            print "{0}: Download failed!".format(link)
            return False
        for block in response.iter_content(1024):
            if not block:
                break
            handle.write(block)
    return True


def parse_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    return [line.strip().split(',') for line in lines]


if __name__ == '__main__':
    links = parse_file('links.txt')
    base = 'libs'
    for directory, link in links:
        download_link(link, os.path.join(base, directory))
    for link in google.get_urls():
        download_link(link, os.path.join(base, 'google-cdn'))
    for link in ajax.get_urls():
        download_link(link, os.path.join(base, 'ajax-cdn'))
