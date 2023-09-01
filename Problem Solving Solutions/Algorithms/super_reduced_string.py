#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    # Write your code here
    newStr = list()
    for i in range(len(s)):
        if s[i] not in newStr:
            newStr.append(s[i])
        elif s[i] in newStr:
            if s[i] == newStr[-1]: 
                newStr.pop()
            else:
                newStr.append(s[i])
    if len(newStr) == 0: return("Empty String")
    else: return("".join(newStr))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
