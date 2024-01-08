#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list = [0, 0, 0, 0]
    count = 0
    for x in tuple_a:
        if count < 2:
            list[count] = x
            count += 1
        else:
            break

    for x in tuple_b:
        if count < 4:
            list[count] = x
            count += 1
        else:
            break

    sum1 = list[0] + list[2]
    sum2 = list[1] + list[3]
    return (sum1, sum2)
