#!/usr/bin/python3
"""
The Holberton School staff evaluates candidates applying for a back-end
position with multiple technical challenges, like this one
"""
from requests import get
import sys


if __name__ == "__main__":
    urls = 'https://api.github.com/repos/{}/{}/commits'.format(
            sys.argv[2], sys.argv[1])
    req = get(urls)
    json_obj = req.json()
    for i in range(0, 10):
        sha = json_obj[i].get('sha')
        name = json_obj[i].get('commit').get('author').get('name')
        print("{}: {}".format(sha, name))
