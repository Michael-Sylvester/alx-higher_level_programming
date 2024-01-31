#!/usr/bin/python3
"""Module to find the max integer in a a_list
"""


def max_integer(a_list=[]):
    """Function to find and return the max integer in a a_list of integers
        If the a_list is empty, the function returns None
    """
    if not isinstance(a_list, list):
        raise TypeError("a_list must be a list")
    
    if len(a_list) == 0:
        return None
    
    for mem in a_list:
        if not isinstance(mem, int):
            raise TypeError("a_List must contain integers")
    
    result = a_list[0]
    i = 1
    while i < len(a_list):
        if a_list[i] > result:
            result = a_list[i]
        i += 1
    return result

print(max_integer([1, 2, 3, 4]))
print(max_integer([1, 3, 4, 2]))