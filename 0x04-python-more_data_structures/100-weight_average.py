#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    scors = [score*weight for (score, weight) in my_list]
    return sum(scors) / sum([weight for (score, weight) in my_list])
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    scors = [score*weight for (score, weight) in my_list]
    return sum(scoes) / sum([weight for (score, weight) in my_list])
