#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    arg_num = len(argv)

    sum = 0

    for x in range(1, arg_num):
        sum = sum + int(argv[x])
    print("{}".format(sum))
