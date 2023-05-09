#!/usr/bin/python3
for x in range(ord('a'), ord('z') + 1):
    if x is not (ord('q')) and x is not (ord('e')):
        print("{}".format(chr(x)), end='')
