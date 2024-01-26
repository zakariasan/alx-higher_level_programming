#!/usr/bin/python3
"""Write a Python script that fetches"""
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    html_content = response.read()
    print("Body response:")
    print("         - type: {}".format(type(html_content)))
    print("         - content: {}".format(html_content))
    print("         - utf8 content: {}".format(html_content.decode('utf-8')))
