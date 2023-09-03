#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays the value
of the variable X-Request-Id in the response header
    - must use the packages requests and sys
    - not allow to import other packages than requests and sys
    - value of this variable is different for each request
    - don’t need to check script arguments (number and type)
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    headers = req.headers
    print(headers.get('X-Request-Id'))
