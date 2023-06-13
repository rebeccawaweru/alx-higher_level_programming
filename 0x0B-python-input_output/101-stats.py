#!/usr/bin/python3
"""Script that reads input from stdin line by line and computes metrics"""
import sys


def get_stats(size, status_codes):
    """Print metrics"""
    print("File size: {}".format(size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    size = 0
    counter = 0
    status_codes = {}
    codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    try:
        for line in sys.stdin:
            if counter == 10:
                get_stats(size, status_codes)
                counter = 1
            else:
                counter += 1

            line = line.split()
            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass
        get_stats(size, status_codes)
    except KeyboardInterrupt:
        get_stats(size, status_codes)
        raise
