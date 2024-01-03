#!/usr/bin/python3
def fizzbuzz():
    """
    Prints numbers from 1 to 100 according to FizzBuzz rules.

    Returns:
    - None
    """
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz", end=" ")
        elif num % 3 == 0:
            print("Fizz", end=" ")
        elif num % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(num, end=" ")
