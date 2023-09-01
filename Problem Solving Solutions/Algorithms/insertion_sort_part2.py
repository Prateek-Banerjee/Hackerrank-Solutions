#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    # Write your code here
    i = 1            
    while i<=(len(arr) - 1):
        elem = arr[i]
        for j in range(i, -1, -1):
            if elem < arr[j]:
                if arr.count(elem) == 1:
                    arr.remove(elem)
                    arr.insert(j, elem)
                elif arr.count(elem) > 1:
                    arr.insert(j, elem)
                    arr.pop(len(arr) - 1 - arr[::-1].index(elem))                    
        i+=1
        print(*arr)
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
