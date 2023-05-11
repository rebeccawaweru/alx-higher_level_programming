#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv
    x = len(argv) - 1
    if x == 0:
        print("0 arguments.")
    elif x == 1:
        print("{} argument:".format(x))
    else:
        print("{} arguments:".format(x))
    for y in range(x):
        print("{}: {}".format(y + 1, argv[y + 1]))
