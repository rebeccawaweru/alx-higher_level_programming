#!/usr/bin/python3
"""
Takes two argument to solve challenge
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    r = requests.get('htpps://api.github.com/repos/{}/{}/commits'
                     .format(argv[2], argv[1]))
    commits = r.json()
    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
