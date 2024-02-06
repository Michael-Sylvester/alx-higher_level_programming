#!/usr/bin/python3
"""Module for appending from files"""
import json


def from_json_string(my_str):
    """File to write text to a file"""
    json_data = json.loads(my_str)
    return json_data


if __name__ == "__main__":
    pass
