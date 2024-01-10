#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    sum = 0
    roman = dict(I = 1, V = 5, X = 10, L = 50, C = 100, D = 1000)
    for letter in roman_string:
        sum += roman[letter]
    return sum
