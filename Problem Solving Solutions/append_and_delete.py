#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here
    common_length = min(len(s), len(t))
    common_prefix = 0

    for i in range(common_length):
        if s[i] != t[i]:
            break
        common_prefix += 1

    total_moves_required = len(s) + len(t) - 2 * common_prefix

    if total_moves_required <= k:
        if (k - total_moves_required) % 2 == 0 or k >= len(s) + len(t):
            return ("Yes")
    
    return ("No")


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
