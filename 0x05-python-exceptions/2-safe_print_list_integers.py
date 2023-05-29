#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    try:
        for y in range(x):
            if isinstance(my_list[y], int):
                print("{:d}".format(my_list[y]), end="")
                counter += 1
    except IndexError:
        if (counter < x):
            raise IndexError("list index out of range") from None
    print()
    return counter
