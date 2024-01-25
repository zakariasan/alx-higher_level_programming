#!/bin/bash
#Write a Bash script that takes in a URL, sends a request to that URL
curl -s -X PUT --data "You got me!" 0.0.0.0:5000/catch_me > /dev/null
