#!/bin/bash
#Write a Bash script that takes in a URL, sends a request to that URL
response=$(curl -s 0.0.0.0:5000/catch_me)

if [[ $response == *"You got me!"* ]]; then
    printf "Server response: You got me!\n"
else
    printf "Error: Server response does not contain the expected message.\n"
fi
