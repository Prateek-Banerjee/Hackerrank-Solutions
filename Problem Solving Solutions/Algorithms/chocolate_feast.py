#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'chocolateFeast' function below.
#
# The function is expected to return (an INTEGER.)
# The function accepts following parameters:
#  1. INTEGER n (initial money that bobby has)
#  2. INTEGER c (cost of each chocolate)
#  3. INTEGER m (the number of wrappers that must be returne(d in order to get a free chocolate))
#

def chocolateFeast(n, c, m):
    # Write your code here
    tce,nw,nc,rw = 0,0,0,0
    tce = tce + (n//c)
    nw = n//c
    if m<=nw:
        if nw == m:
            tce+=1
        while nw>m:
            nc = nw//m
            tce+=nc
            rw = nw%m
            nw = (nw//m)+rw
            if nw == m:
                tce+=1
                break           
        return(tce)
    else:
        return(tce)
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        c = int(first_multiple_input[1])

        m = int(first_multiple_input[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
