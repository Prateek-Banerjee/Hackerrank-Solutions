#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import zip_longest
#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    newString = "".join(s.split())
    floorLen = math.floor(len(newString)**0.5) # rows
    ceilLen = math.ceil(len(newString)**0.5)   # columns
    listlnewString = list(newString[0+i:ceilLen+i] for i in range(0, len(newString), ceilLen))
    finalS = str()
    for i in list(zip_longest(*listlnewString,fillvalue="")):
        finalS += ("".join(i)+" ")
    return finalS

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
