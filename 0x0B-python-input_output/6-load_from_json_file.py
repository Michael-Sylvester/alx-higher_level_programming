#!/usr/bin/python3
"""Module for loading from json files"""
import json


def load_from_json_file(filename):
    """Function for converting file data from json format to object"""
    with open(filename, 'r', encoding="utf-8") as file:
        data = json.load(file)
    return data


if __name__ == "__main__":
    pass
