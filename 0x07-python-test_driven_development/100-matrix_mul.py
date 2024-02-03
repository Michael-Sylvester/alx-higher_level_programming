#!/usr/bin/python3
"""Module for matrix multiplication"""


def matrix_mul(m_a, m_b):
    """Function that multiplies 2 matrixes agaist themselves"""

    runchecks(m_a, m_b)
    m_c = list()
    height = len(m_a[0])
    width = len(m_b)
    x1, x2, y1, y2 = 0, 0, 0, 0
    while (x1 < len(m_a)):
        temp = list()
        while y2 < len(m_b[0]):
            sum = 0
            while y1 < height:
                sum += m_a[x1][y1] * m_b[x2][y2]
                y1 += 1
                x2 += 1
            temp.append(sum)
            sum, y1, x2 = 0, 0, 0
            y2 += 1
        y2 = 0
        x1 += 1
        m_c.append(temp)

    return m_c


def runchecks(m_a, m_b):
    """Checks for all Errors"""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for mem in m_a:
        if not isinstance(mem, list):
            raise TypeError("m_a must be a list of lists")
    for mem in m_b:
        if not isinstance(mem, list):
            raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for mem in m_a:
        for lilmem in mem:
            if not isinstance(lilmem, int) and not isinstance(lilmem, float):
                raise TypeError("m_a should contain only integers or floats")
    for mem in m_b:
        for lilmem in mem:
            if not isinstance(lilmem, int) and not isinstance(lilmem, float):
                raise TypeError("m_b should contain only integers or floats")

    lenth = len(m_a[0])
    for mem in m_a:
        if len(mem) != lenth:
            raise TypeError("each row of m_a must be of the same size")
    lenth = len(m_b[0])
    for mem in m_b:
        if len(mem) != lenth:
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
