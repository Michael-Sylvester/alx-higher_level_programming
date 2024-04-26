#!/bin/bash
#Display body of status 200 url respons
curl -s -o /dev/null -w "%{http_code}" $1 | grep -q "200" && curl -s  $1
