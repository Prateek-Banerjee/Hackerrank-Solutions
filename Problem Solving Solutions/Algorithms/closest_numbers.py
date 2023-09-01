#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    # Write your code here
    arr.sort()
    newArr = [arr[0],arr[1]]
    minDiff = (arr[1]-arr[0])
    for i in range(1,len(arr)-1):
        if (arr[i+1]-arr[i])==minDiff:
            newArr.append(arr[i])
            newArr.append(arr[i+1])      
        elif (arr[i+1]-arr[i])<minDiff:
            newArr.clear()
            newArr.append(arr[i])
            newArr.append(arr[i+1])
            minDiff = (arr[i+1]-arr[i])                
    return newArr
           
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()