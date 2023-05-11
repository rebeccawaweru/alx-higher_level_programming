#!/usr/bin/python3

if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    import sys
    num = sys.argv
    if len(num) != 4:
        print("Usage: {:s} <a> <operator> <b>".format(num[0]))
        sys.exit(1)
    x = int(num[1])
    operator = num[2]
    z = int(num[3])

    final = None

    if operator == "+":
        final = add(x, z)
    elif operator == "-":
        final = sub(x, z)
    elif operator == "*":
        final = mul(x, z)
    elif operator == "/":
        final = div(x, z)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print(f"{x} {operator} {z} = {final}")
    sys.exit(0)
