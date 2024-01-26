#!/usr/bin/python3
"""Write a Python script that takes in a letter and sends a POST request"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    url = 'http://0.0.0.0:5000/search_user'
    payload = {'q': letter}

    try:
        response = requests.post(url, data=payload)
        data = response.json()

        if data:
            print("[{}] {}".format(data['id'], data['name']))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
