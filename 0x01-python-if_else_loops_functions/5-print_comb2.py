#!/usr/bin/python
for k in range(100):
    print(f"{k:02}", end=", " if k < 99 else "\n")#{.02}formats number to always be 2 digits,(, ) in end control what comes after each number