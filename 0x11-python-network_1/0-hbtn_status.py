#!/usr/bin/python3
""" 0-hbtn_status module """
import urllib.request

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    content = response.read()

    print('Body response:')
    print(f'\t - type: {type(content)}')
    print(f'\t - content: {content}')
    print(f'\t - utf8 content: {content.decode("utf-8")}')
