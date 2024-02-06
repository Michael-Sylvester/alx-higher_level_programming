#!/usr/bin/python3
"""module for child class Myint"""


class MyInt(int):
    def __eq__(self, __value: object) -> bool:
        return super().__ne__(__value)
    
    def __ne__(self, __value: object) -> bool:
        return super().__eq__(__value)
