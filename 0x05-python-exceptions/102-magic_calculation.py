#!/usr/bin/python3
def magic_calculation(a, b):
    final = 0
    for j in range(1, 3):
        try:
            if j > a:
                raise Exception("Too far")
            else:
                final += a ** b / j
        except IndexError:
            final = b + a
            break
    return final
