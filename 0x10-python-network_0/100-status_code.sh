#!/bin/bash
#Display reponse status code without using ; && or |
curl -s -o /dev/null -w "%{http_code}" $1
