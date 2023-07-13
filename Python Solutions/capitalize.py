#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):    
    ns = []
    for i in range(len(s.split(" "))):
        ns.append((s.split(" ")[i]).capitalize())
    
    return (" ".join(ns))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
