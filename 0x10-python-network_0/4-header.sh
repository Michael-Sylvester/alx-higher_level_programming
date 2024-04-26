#!/bin/bash
# This script sends a GET request to the specified URL, including a header X-School-User-Id with the value 98, and displays the body of the response
curl -s -H "X-School-User-Id: 98" "$1"
