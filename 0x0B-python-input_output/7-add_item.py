#!/usr/bin/python3
"""Module for reading and writing dta to a json file"""
import json
import sys
import os
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def addnewline(filename):
    """adds new line to end of json file"""
    with open(filename, 'a', encoding="utf-8") as f:
        f.write('\n')


filename = "add_item.json"

if not os.path.exists(filename):
    newlist = list()
    save_to_json_file(newlist, filename)
    addnewline(filename)
    print("New {} file created".format(filename))
else:
    print("opening {}".format(filename))
    filelist = list(load_from_json_file(filename))
    if len(sys.argv) > 1:
        print("Command line arguments found.\nAdding to {}".format(filename))
        for i in range(1, len(sys.argv)):
            filelist.append(sys.argv[i])
        save_to_json_file(filelist, filename)
        addnewline(filename)
