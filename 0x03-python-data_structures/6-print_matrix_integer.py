#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for mem in matrix:
        for elem in mem:
            print("{:d} ".format(elem), end="")
        print("")
