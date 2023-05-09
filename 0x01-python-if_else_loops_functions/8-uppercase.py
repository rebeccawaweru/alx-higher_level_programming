#!/usr/bin/python3
def uppercase(str):
    y = ""
    for x in str:
        if ord('a') <= ord(x) <= ord('z'):
            y += chr(ord(x) - 32)
        else:
            y += x
    print("{}".format(y))
