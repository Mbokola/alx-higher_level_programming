#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays the body
of the response.
    - If the HTTP status code is greater than or equal to 400, print:
      Error code: followed by the value of the HTTP status code
    - must use the packages requests and sys
    - not allowed to import packages other than requests and sys
    - don’t need to check arguments passed to the script (number or type)
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    code = req.status_code
    if code >= 400:
        print(f"Error code: {code}")
    else:
        print(req.text)
