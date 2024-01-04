#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    dirlist = dir(hidden_4)
    size = len(dirlist)

    for x in range(0, size):
        if dirlist[x][0] != "_":
            print("{}".format(dirlist[x]))
