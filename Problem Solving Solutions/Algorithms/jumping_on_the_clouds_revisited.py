#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    iniChg = 100
    it = 0
    while True:
        it = (it+k)%(len(c))
        if c[it] == 0: iniChg-=1
        elif c[it] == 1: iniChg-=3
    
        if it == 0: break    
    return iniChg

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
