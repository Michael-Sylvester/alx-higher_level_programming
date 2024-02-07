#!/usr/bin/python3
"""Module for changing class to json rep"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Initializer"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns dict representation of Student"""
        return dict(self.__dict__)
