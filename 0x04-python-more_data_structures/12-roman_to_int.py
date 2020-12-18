#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or roman_string is None):
        return (0)
    dic_num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    n = 0
    for i in range(len(roman_string)):
        if dic_num.get(roman_string[i], 0) == 0:
            return (0)
        if (i != (len(roman_string) - 1) and
        dic_num[roman_string[i]] < dic_num[roman_string[i + 1]]):
            n += dic_num[roman_string[i]] * -1
        else:
            n += dic_num[roman_string[i]]
    return (n)
