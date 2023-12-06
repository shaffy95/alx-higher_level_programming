#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence != '':
        value_of_char = sentence[0]
    else:
        value_of_char = None
    return (len(sentence), value_of_char)
