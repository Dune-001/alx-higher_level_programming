#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4) #get all names defined in hidden_4
    filtered_names = sorted(name for name in names if not name.startswith("__")) #filter and sort names ignore those starting with '__'
    for name in filtered_names:
        print(name)

