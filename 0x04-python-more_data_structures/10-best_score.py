#!/usr/bin/python3
def best_score(a_dictionary):
    biggest = None
    val = 0
    if type(a_dictionary) is dict:
        for (key, value) in a_dictionary.items():
            if value > val:
                val = value
                biggest = key
    return biggest
