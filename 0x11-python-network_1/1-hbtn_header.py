#!/usr/bin/python3
"""
Script that takes in Url, sends a request to the URL
and displays the value of the X-Request-Id variable
"""
if __name__ == "__main__":
    from urllib import request
    from sys import argv
    req = request.Request(argv[1])
    with request.urlopen(req) as r:
        print(r.headers.get('X-Request-Id'))
