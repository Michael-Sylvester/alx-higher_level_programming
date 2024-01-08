#!/usr/bin/python3
def multiple_returns(sentence):
    size = len(sentence)
    if size > 0:
        first = sentence[0]
    else:
        first = None
    return (size, first)
