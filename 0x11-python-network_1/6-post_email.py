#!/usr/bin/python3
"""
Takes a url and email and sends a POST request to the passed
URL with the email as a parameter and displays the body
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    dt = {'email': argv[2]}
    r = requests.post(argv[1], data=dt)
    print(r.text)
