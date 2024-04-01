#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL
and displays the body
"""
import urllib.request
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            content_html = response.read()
            print(content_html.decode('utf-8'))
    except urllib.error.HTTPError as error_code:
        print("Error code: {}".format(error_code.code))
