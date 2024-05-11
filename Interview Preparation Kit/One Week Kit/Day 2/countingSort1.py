#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
from collections import Counter
""" def countingSort(arr):
    # Write your code here """
arr = [1,1,3,2,1]
newArr = sorted(arr)
maximum = max(newArr)

occurrence = dict()

for i in range(maximum+1):
    if i in occurrence.keys():
        occurrence[i] = occurrence.get(i) + 1
    elif i not in occurrence.keys():
        occurrence[i] = 0

print(occurrence.values())

""" if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close() """
