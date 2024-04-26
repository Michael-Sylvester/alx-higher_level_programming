#!/bin/bash
#Display all methodes
curl -sI -X OPTIONS 0.0.0.0:5000 | grep "Allow" | awk '{$1=""; sub(/^ /, ""); print $0}'
