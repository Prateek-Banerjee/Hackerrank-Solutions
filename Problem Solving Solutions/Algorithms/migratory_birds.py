#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    frequencies = defaultdict(int)
    birds = {}
    max_freq = 0
    for bird in arr:
        frequencies[bird] += 1
        birds[frequencies[bird]] = min(bird, birds.get(frequencies[bird], math.inf))
        max_freq = max(max_freq, frequencies[bird])   
    return birds[max_freq]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
