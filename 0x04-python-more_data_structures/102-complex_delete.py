#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys  = list(a_dictionary)
    newdict = dict()
    for key in keys:
        if a_dictionary[key] == value:
            del a_dictionary[key]
        else:
            newdict[key] = a_dictionary[key]
    return newdict
