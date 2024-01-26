#!/usr/bin/python3
"""Write a Python script that takes your GitHub credentials """
from requests import get, auth
import sys


if __name__ == "__main__":
    request = get('https://api.github.com/user',
                  auth=auth.HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    print(request.json().get('id'))
