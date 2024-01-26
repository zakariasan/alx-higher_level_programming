#!/usr/bin/python3
"""Write a Python script that fetches"""
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    html_content = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(html_content)))
    print("\t- content: {}".format(html_content))
    print("\t- content: {}".format(html_content.decode('utf-8')))
