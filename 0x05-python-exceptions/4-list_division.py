#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    ans = 0
    index = 0
    anslist = list()
    while index < list_length:
        try:
            ans = my_list_1[index] / my_list_2[index]
        except IndexError:
            print("out of range")
            ans = 0
        except TypeError:
            print("wrong type")
            ans = 0
        except ZeroDivisionError:
            print("division by 0")
            ans = 0
        finally:
            anslist.append(ans)
            index += 1
    return anslist
