#!/bin/python3
# DONE FROM GEEKS FOR GEEKS
import math
import os
import random
import re
import sys

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

def squares(a, b):
    # Write your code here
    return (math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()


"""
def squares(a, b):
    # Write your code here
    count = 0
    for i in range(a,b+1):
        if int(((str(math.sqrt(i))).split('.'))[1]) == 0 and len(((str(math.sqrt(i))).split('.'))[1]) == 1:
            count+=1
    return count
"""