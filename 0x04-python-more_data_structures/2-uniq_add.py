#!/usr/bin/python3
def uniq_add(my_list=[]):
    listset = set(my_list)
    sum = 0
    for memb in listset:
        sum += memb
    return sum
