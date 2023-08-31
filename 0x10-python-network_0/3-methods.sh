#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -sI -X OPTIONS "$1" | sed -n 's/^Allow: \(.*\)/\1/p'
