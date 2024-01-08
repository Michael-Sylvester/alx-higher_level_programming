#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for mem in matrix:
        for e in range(len(mem)):
            print("{:d}".format(mem[e]), end="")
            if e != len(mem) - 1:
                print("", end=" ")
        print("")
