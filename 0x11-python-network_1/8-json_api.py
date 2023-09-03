#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
    - letter must be sent in the variable q
    - If no argument is given, set q=""
    - If the response body is properly JSON formatted and not empty,
          - display the id and name like this: [<id>] <name>
          - Otherwise:
               - Display Not a valid JSON if the JSON is invalid
               - Display No result if the JSON is empty

    - must use the package requests and sys
    - not allowed to import packages other than requests and sys
"""

import sys
import requests

if __name__ == "__main__":
    if sys.argv[1]:
        letter = sys.argv[1]
    else:
        letter = ""

    data = dict(q=letter)
    url = "http://0.0.0.0:5000/search_user"
    post_response = requests.post(url, data=data)

    if post_response.headers.get('Content-Type') == 'application/json':
        json_data = post_response.json()
        if json_data:
            print(f"[{json_data['id']}] {json_data['name']}")
        else:
            print("No result")
    else:
        print("Not a valid JSON")
