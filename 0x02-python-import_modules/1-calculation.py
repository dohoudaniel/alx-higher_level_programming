#!/usr/bin/python3

if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div

    # Define variables
    a = 10
    b = 5

    # Typecasting
    a = int(a)
    b = int(b)

    # Printing the result
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
