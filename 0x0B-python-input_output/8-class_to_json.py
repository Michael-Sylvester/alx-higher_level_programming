#!/usr/bin/python3
"""Module for loading from json files"""
import json


def class_to_json(obj):
    return json.dumps(obj.__dict__)
