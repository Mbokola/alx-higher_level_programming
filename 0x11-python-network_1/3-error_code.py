#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays the body
of the response (decoded in utf-8).
    - manage urllib.error.HTTPError exceptions and print: Error code:
      followed by the HTTP status code
    - must use the packages urllib and sys
    - not allowed to import other packages than urllib and sys
    - don’t need to check arguments passed to the script (number or type)
    - must use the with statement
"""

import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError

if __name__ == "__main__":
    url = sys.argv[1]
    req = Request(url)
    try:
        with urlopen(req) as response:
            content = response.read().decode("utf-8")
            print(content)
    except HTTPError as err:
        print(f"Error code: {err.code}")
