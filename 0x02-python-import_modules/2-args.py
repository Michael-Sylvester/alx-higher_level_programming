#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    arg_num = len(argv)

    if arg_num == 1:
        print("0 argument.")
    elif arg_num == 2:
        print("1 argument:")
    else:
        print("{} argumanets:".format(arg_num - 1))

    for x in range(1, arg_num):
        print("{}: {}".format(x, argv[x]))
