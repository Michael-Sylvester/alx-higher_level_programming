#!/usr/bin/python3
def max_integer(my_list=[]):
    size = len(my_list)
    if len == 0:
        return (None)
    else:
        max = my_list[0]
        for x in my_list:
            if x > max:
                max = x
    return (max)
