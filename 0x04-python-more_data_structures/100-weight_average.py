#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return 0
    w_total = 0
    t_weight = 0
    for tup in my_list:
        w_total += tup[0] * tup[1]
        t_weight += tup[1]
    return w_total/t_weight
