#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Write your code here
    avssc = dict((Counter(a)))
    minDist = 1000
    if any(i>1 for i in avssc.values()):
        for j in a:
            if a.count(j)>1:
                index = [k for k,val in enumerate(a) if val==j]
                if index[1]-index[0] < minDist:
                    minDist  = index[1]-index[0]
        
        return (minDist)
    else:
        return ("-1")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
