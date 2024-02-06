#!/usr/bin/python3
"""Module for changing to json format"""
import json


def to_json_string(my_obj):
    """Function to write text in json format"""
    json_data = json.dumps(my_obj)
    return json_data


if __name__ == "__main__":
    pass
