#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    index = 0
    try:
        while (index < x):
            print("{}".format(my_list[index]), end='')
            count += 1
            index += 1
    except IndexError:
        pass
    finally:
        print("")
    return count
