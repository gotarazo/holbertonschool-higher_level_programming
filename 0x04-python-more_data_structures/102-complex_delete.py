#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary is not None and type(a_dictionary) is dict:
        item = a_dictionary.item()
        delet = {key: val for (key, val) in items if value == val}
        for (key, val) in delet.items():
            del a_dictionary[key]
        return a_dictionary.copy()
