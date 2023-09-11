#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'canConstruct' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY a as parameter.
#

def canConstruct(a):
    # Return "Yes" or "No" denoting whether you can construct the required number.
    if len(a) == 1:
        if (a[0])%3 == 0: return "Yes"
        else: return "No"
    else:
        sums = 0
        for nums in a:
            sums += (sum(int(i) for i in str(nums)))
        if sums%3 == 0: return "Yes"
        else: return "No"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        a = list(map(int, input().rstrip().split()))

        result = canConstruct(a)

        fptr.write(result + '\n')

    fptr.close()
