#!/usr/bin/python3
"""
script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
    - must use Basic Authentication with a personal access token as password to
      access to your information (only read:user permission is needed)
    - The first argument will be your username
    - The second argument will be your password (in your case, a personal
      access token as password)
    - must use the package requests and sys
    - not allowed to import packages other than requests and sys
    - don’t need to check arguments passed to the script (number or type)
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    passwrd = sys.argv[2]
    url = 'https://api.github.com/user'

    # Create a Basic Authentication header with your access token
    auth = HTTPBasicAuth(username, passwrd)
    # Make a GET request to the GitHub API to retrieve your user data
    response = requests.get(url, auth=auth)
    user_data = response.json()
    print(user_data.get('id'))
