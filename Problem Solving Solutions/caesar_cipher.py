#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    newStr = []    
    for i in s:    
        if "a"<= i <="z":
            newStr.append(chr(((ord(i)-97+k)%26)+97))
        elif "A"<= i <="Z":
            newStr.append(chr(((ord(i)-65+k)%26)+65))
        else:
            newStr.append(i)
    return ("".join(newStr))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
