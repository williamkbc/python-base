#!/usr/bin/en python3

import os
import sys

# LBYL  - Look Before You Leap
if os.path.exists("names.txt"):
    print("O arquivo existe") 
    input("...") # Race condition to wait for user input
    names = open("names.txt").readlines()
else:
    print("[Error]: The file 'names.txt' does not exist.")
    sys.exit(1)


if len(names) >= 3:
    print(names[2])
else:
    print("[Error]:There are not enough names in the list.")
    sys.exit(1)
# EAFP - Easier to Ask Forgiveness than Permission