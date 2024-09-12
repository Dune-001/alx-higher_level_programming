#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return (str)# return original string if n is out of range
    return (str[:n] + str[n+1:])