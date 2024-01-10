#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newlist = []
    for memb in my_list:
        if memb == search:
            newlist.append(replace)
        else:
            newlist.append(memb)
    return newlist
