#!/usr/bin/python3
def no_c(my_string):
    new_string = "" #store the result
    for char in my_string: #loop through each char in string
        if char != 'c' and char != 'C':
            new_string += char #append new string without any c and C
    return (new_string)
