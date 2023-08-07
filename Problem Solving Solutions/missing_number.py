#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def missingNumbers(arr, brr):
    # Write your code here
    d=dict()
    
    for element in arr:
        if element in d:
            d[element]+=1 
        else:
            d[element]=1
        
    missing=set() 
    for element in brr:
        if not element in d:
            missing.add(element)
        else:
            if d[element]>=1:
                d[element]-=1
            else:
                missing.add(element)
    
    return sorted(list(missing))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
"""
    numbers = []
    for i in brr:
        if i not in numbers:
            if i not in arr:            
                numbers.append(i)
            else:
                if brr.count(i) != arr.count(i):
                    numbers.append(i)
    numbers.sort()
    return (numbers)
"""