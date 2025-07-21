#!/usr/bin/en python3

import os
import sys

# EAFP - Easier to Ask Forgiveness than Permission
# (É mais fácil pedir perdão do que permissão)

try:  
    names = open("names.txt").readlines()
    # FileNotFoundError
except FileNotFoundError as e:
    print(f"{str(e)}.")
    sys.exit(1) 
    # TODO: usar retry
else:
    print("File opened successfully.")
finally:
    print("This will always execute, regardless of success or failure.")

try:
    print(names[2])
except:
    print("[Error]:There are not enough names in the list.")
    sys.exit(1)
