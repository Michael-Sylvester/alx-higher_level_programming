#!/usr/bin/python3
"""Module for changing class to json rep and back"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Initializer"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dict representation of Student"""
        if attrs is None:
            return dict(self.__dict__)
        else:
            newd = dict()
            old = dict(self.__dict__)
            keys = old.keys()
            for att in attrs:
                if att in keys:
                    newd.update({att: old.get(att)})
            return newd

    def reload_from_json(self, json):
        """Sets new attribut values from json dict"""
        keylist = json.keys()
        for key in keylist:
            setattr(self, key, json.get(key))
