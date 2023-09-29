#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'larrysArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY A as parameter.
#

def larrysArray(A):
    # Write your code here
    """
    The trick is to check whether each number at a particular index in the array is larger then any of its following 
    numbers or not. If it larger then increment a counter by 1. Repeat the same process for the whole list, and once
    the list is traversed, check whether the counter value is divisible by 2 or not. If it is divisible by 2 then it
    means the after performing the rotations, the array can be sorted and it is not divisible by 2 then it cannot be sorted.
    """
    rotations = 0
    for num1 in range(len(A)):
        for num2 in range(num1, len(A)):
            if A[num1]>A[num2]:
                rotations+=1
    
    if rotations % 2 == 0:
        return "YES"
    else:
        return "NO"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
