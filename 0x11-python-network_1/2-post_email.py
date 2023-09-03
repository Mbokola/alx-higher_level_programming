#!/usr/bin/python3
"""
2-post_email module -  sends a POST request to the passed URL with the email
as a parameter, and displays the body of the response (decoded in utf-8)
"""

import sys
import urllib.request

if __name__ == '__main__':
    url = sys.argv[1]
    data = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(data)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
