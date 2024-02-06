#!/usr/bin/python3
"""Module for appending from files"""
import json


def save_to_json_file(my_obj, filename):
    """File to write text to a file"""
    with open(filename, 'w', encoding="utf-8") as json_file:
        json.dump(my_obj, json_file)
   


if __name__ == "__main__":
    pass
