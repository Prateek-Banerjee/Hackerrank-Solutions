#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    # Write your code here
    if len(s)%2 != 0:
        return (-1)
    else:
        s1 = sorted(s[0:len(s)//2])
        s2 = sorted(s[len(s)//2:])
        if s1 == s2:
            return (0)        
        else:
            for i in s2:
                try:
                    s1.pop(s1.index(i))
                except:
                    continue
            return(len(s1))
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
