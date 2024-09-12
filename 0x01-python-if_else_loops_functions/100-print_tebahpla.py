#!/usr/bin/python3
for k in range(26):
    print(f"{chr(122 - k) if k % 2 == 0 else chr(122 - k - 32)}", end="")