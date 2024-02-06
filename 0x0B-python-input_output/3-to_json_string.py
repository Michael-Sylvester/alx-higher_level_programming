#!/usr/bin/python3
"""Module for appending from files"""
import json


def to_json_string(my_obj):
    """File to write text to a file"""
    json_data = json.dumps(my_obj)
    return json_data


if __name__ == "__main__":
    pass
