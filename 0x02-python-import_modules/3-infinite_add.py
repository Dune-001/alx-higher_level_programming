#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv[1:] #exclude name of the script
    num_argz = 0
for arg in argv: #add all ars after converting them to int
    num_argz += int(arg)
print(num_argz)
