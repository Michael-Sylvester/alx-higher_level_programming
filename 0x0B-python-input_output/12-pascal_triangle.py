#!/usr/bin/python3
"""Module for changing class to json rep and back"""


def pascal_triangle(n):
    """Draws th rows of pascals triangle as a list of lists"""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle


if __name__ == "__main__":
    pass
