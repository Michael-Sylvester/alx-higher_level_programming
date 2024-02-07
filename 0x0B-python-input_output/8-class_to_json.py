#!/usr/bin/python3
"""Module for changing class to json rep"""


def class_to_json(obj):
    return {attr: getattr(obj, attr) for attr in vars(obj)}
