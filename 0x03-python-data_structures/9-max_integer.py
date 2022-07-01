#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    max = my_list[0]

    for index, digit in enumerate(my_list):
        if my_list[index] > max:
            max = digit
    return max
