#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keyset = list(a_dictionary)
    keyset.sort()
    for key in keyset:
        print("{}: {}".format(key, a_dictionary.get(key)))
