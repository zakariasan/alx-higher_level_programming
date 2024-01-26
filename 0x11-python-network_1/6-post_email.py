#!/usr/bin/python3
"""Write a Python script that takes in a URL and an email address,
sends a POST"""
import requests
import sys


if __name__ == "__main__":
    params = {'email': sys.argv[2]}
    req = requests.post(sys.argv[1], data=params)
    print(req.text)
