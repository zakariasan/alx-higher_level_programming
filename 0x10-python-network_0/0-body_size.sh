#!/bin/bash
#Write a Bash script that takes in a URL, sends a request to that URL
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r\n'
