#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def solve(n):
    # Write your code here
    sumOfDigitsOfN = sum(int(i) for i in str(n))
    primeFactors = []
    i = 2
    while i<=n:
        if n%i:
            i+=1
        else:
            n//=i
            primeFactors.append(i)
    sumOfDigitsOfPrimeFactors = 0
    for factor in primeFactors:
        sumOfDigitsOfPrimeFactors += sum(int(digit) for digit in str(factor))
    if sumOfDigitsOfN == sumOfDigitsOfPrimeFactors: return 1
    else: return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = solve(n)

    fptr.write(str(result) + '\n')

    fptr.close()
