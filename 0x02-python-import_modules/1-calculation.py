#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5
    print("{} + {} = {}".formtat(a, b, add(a, b)))
    print("{} - {} = {}".formtat(a, b, sub(a, b)))
    print("{} * {} = {}".formtat(a, b, mul(a, b)))
    print("{} / {} = {}".formtat(a, b, div(a, b))) 
