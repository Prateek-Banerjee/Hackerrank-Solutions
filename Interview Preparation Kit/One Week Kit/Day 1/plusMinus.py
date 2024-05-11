#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    cpos = cneg = czero = 0
    for i in arr:
        if i == 0: czero += 1
        elif i > 0: cpos += 1
        elif i < 0: cneg += 1
    
    print(cpos/len(arr), "\n", cneg/len(arr), "\n", czero/len(arr))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
