#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == 0:
        return (None)
    max_value = my_list[0]
    for k in my_list:
        if k > max_value:
            max_value = k
    return (max_value)
