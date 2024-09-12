#!/usr/bin/python
for k in range(10):
    for i in range(k + 1, 10):#ensures i > k so that 01 and 10 aren't duplicated
        print(f"{k}{i}", end=", " if k != 8 or i != 9 else "\n")