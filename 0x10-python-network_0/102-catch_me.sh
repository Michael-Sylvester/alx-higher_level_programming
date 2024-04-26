#!/bin/bash
# Sends a POST request to 0.0.0.0:5000/catch_me with the user agent "You got me!"
curl -s -X POST -d "You got me!" http://0.0.0.0:5000/catch_me
