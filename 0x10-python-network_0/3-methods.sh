#!/bin/bash
#Display all methodes
curl -sI -X OPTIONS $1 | grep "Allow" | awk '{$1=""; sub(/^ /, ""); print $0}'
