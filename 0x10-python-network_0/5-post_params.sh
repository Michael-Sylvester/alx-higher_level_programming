#!/bin/bash
# This script sends a POST request to the specified URL, including variables email and subject with the given values, and displays the body of the response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
