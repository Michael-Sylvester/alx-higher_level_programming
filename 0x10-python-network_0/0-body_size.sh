#!/bin/bash
#Display body size of url response
curl -sI $1 | grep -i "Content-Length" | awk '{print $2}'
