#!/usr/bin/python3
"""  1-hbtn_header - displays the value of the X-Request-Id """

import sys
import urllib.request

if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as response:
        headers = response.headers
        print(headers.get('X-Request-Id'))
