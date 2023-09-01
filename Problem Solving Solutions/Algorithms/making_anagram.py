#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makingAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def makingAnagrams(s1, s2):
    # Write your code here
    s1List = list(s1)
    s2List = list(s2)
    count = 0
    if s1List == s2List:
        return (0)        
    else:
        for i in s1List:
            try:
                index = s2List.index(i)
                s2List.pop(index)
                count+=1
            except:
                continue
        return((len(s1)+len(s2))-(count*2))    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
