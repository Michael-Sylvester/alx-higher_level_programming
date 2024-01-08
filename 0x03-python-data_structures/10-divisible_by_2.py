#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    answer = []
    for x in my_list:
        if my_list[x] % 2 == 0:
            answer.append(True)
        else:
            answer.append(False)
    return answer
