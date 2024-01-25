#!/bin/bash
#Write a Bash script that takes in a URL, sends a request to that URL
curl -s -L -X HEAD -w "%{http_code}" "$1"
