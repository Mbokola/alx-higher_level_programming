#!/usr/bin/python3
"""
script that takes in a URL and an email address, sends a POST request to
the passed URL with the email as a parameter, and finally displays the
body of the response.
    - email must be sent in the variable email
    - must use the packages requests and sys
    - not allowed to import packages other than requests and sys
    - don’t need to error check arguments passed to the script (number or type)
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    data = dict(email=sys.argv[2])
    post_response = requests.post(url, data=data)
    content = post_response.text
    print(content)
