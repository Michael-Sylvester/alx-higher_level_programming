#!/usr/bin/python3
def best_score(a_dictionary):
    dic = a_dictionary
    bestvalue = 0
    best = ""

    if dic is None or len(dic) == 0:
        return None
    elif len(dic) == 1:
        best = list(dic)[0]
    else:
        allkeys = list(dic)
        best = allkeys[0]
        bestvalue = dic[best]
        for key in allkeys:
            if dic[key] > bestvalue:
                bestvalue = dic[key]
                best = key
    return best
