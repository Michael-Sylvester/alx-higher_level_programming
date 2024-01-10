#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newlist = list()

    for lists in matrix:
        templist = list()
        for memb in lists:
            a = memb ** 2
            templist.append(a)
        newlist.append(templist)
    return newlist
