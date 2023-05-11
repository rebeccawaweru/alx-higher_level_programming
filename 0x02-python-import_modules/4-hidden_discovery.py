#!/usr/bin/python3

if __name__ == '__main__':
    import hidden_4
    lst = dir(hidden_4)
    for name in lst:
        if not name.startswith('__'):
            print("{:s}".format(name))
