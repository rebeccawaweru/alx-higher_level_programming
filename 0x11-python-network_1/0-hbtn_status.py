#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status
"""
import urllib.request
if __name__ == '__main__':
    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print('Body response:\n\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf-8 content: {}'.format(html.decode('utf-8')))
