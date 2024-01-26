#!/usr/bin/python3
"""Python modual for division of matrix function"""


def matrix_divided(matrix, div):
    """Function to divide matrix members by div"""
    # check if maatrix is a list
    if not isinstance(matrix, list):
        typeError()

    lenth = len(matrix[1])
    # check if all members of matrix are lists of the same length
    for listmember in matrix:
        if not isinstance(listmember, list):
            typeError()
        if len(listmember) != lenth:
            raise TypeError("Each row of the matrix must have the same size")
        # check if each inner list contains floats/ints
        for mem in listmember:
            if not isinstance(mem, (int, float)):
                typeError()
    # check if div is an int/float not equal to 0
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    # start calculation for new matrix
    newmatrix = []
    for listmember in matrix:
        newmember = []
        for member in listmember:
            newmember.append(round(member/div, 2))
        newmatrix.append(newmember)
    return newmatrix


def typeError():
    """Raises TypeError message"""
    str1 = "matrix must be a matrix (list of lists) "
    str2 = "of integers/floats"
    raise TypeError(str1 + str2)
