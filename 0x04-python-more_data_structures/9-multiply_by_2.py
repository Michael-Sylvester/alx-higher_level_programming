#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdict = dict()
    for key in a_dictionary.keys():
        newdict[key] = a_dictionary[key] * 2
    return newdict
