#!/bin/bash
#Write a Bash script that takes in a URL, sends a request to that URL
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
