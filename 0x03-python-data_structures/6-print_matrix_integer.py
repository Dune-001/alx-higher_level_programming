#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j, num in enumerate(i):
            if j != 0:
                print(" ", end="")
            print("{}".format(num), end="")
        print()
        