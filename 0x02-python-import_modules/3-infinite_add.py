#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv
    num = len(argv) - 1
    total = 0
    for x in range(num):
        total += (int(argv[x + 1]))
    print("{:d}".format(total))
