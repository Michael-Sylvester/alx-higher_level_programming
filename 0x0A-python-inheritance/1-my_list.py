#!/usr/bin/python3
"""module for lookup function"""


class MyList(list):
    """Print new insatnce of list in ascending order"""
    def print_sorted(self):
        order = list()
        for m in self:
            order.append(m)
        order.sort()
        print(order)
