#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    arg_num = len(argv)

    if arg_num == 1:
        print("{} arguments.".format(arg_num - 1))
    elif arg_num == 2:
        print("{} argument:".format(arg_num - 1))
    else:
        print("{} argumanets:".format(arg_num - 1))

    for x in range(1, arg_num):
        print("{}: {}".format(x, argv[x]))
