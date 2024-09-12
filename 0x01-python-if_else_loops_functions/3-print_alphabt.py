#!/usr/bin/python3
for k in range(97, 123):
    if (chr(k) != 'q') and (chr(k) != 'e'):# chr(k) converts ascii to corresponding character
        print(f"{chr(k)}", end="")