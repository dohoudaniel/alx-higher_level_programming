#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    A function that prints a
    matrix of integers
    """
    for i in matrix:
        for j in i:
            print("{}".format(j), end=" ")
        print()