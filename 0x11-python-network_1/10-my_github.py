#!/usr/bin/python3
"""Write a Python script that takes your GitHub credentials """
from requests import get, auth
import sys


if __name__ == "__main__":
    apiurl = 'https://api.github.com/user'
    username = sys.argv[1]
    token = sys.argv[2]
    request = get(apiurl, auth=auth.HTTPBasicAuth(username, token))
    print(request.json().get('id'))
