#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv[1:] #exclude script name from arguments
    num_argz = len(argv)
if num_argz == 0:
    print("0 arguments.")
if num_argz == 1:
    print("1 argument:")
else:
    print(f"{num_argz} arguments:")

for k, arg in enumerate(argv, 1): #print each argument with its position starting from 1
    print(f"{k}: {arg}")