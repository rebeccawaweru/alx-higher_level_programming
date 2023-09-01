#!/usr/bin/python3
"""
Takes url and an email, sends a POST request to the passed
url with the email as a parameter, and displays the body of response
"""
if __name__ == "__main__":
    import urllib.parse as parse
    import urllib.request as request
    from sys import argv
    variables = {'email': argv[2]}
    info = parse.urlencode(variables).encode('utf-8')
    req = request.Request(argv[1], info)
    with request.urlopen(req) as r:
        print(r.read().decode('utf-8'))
