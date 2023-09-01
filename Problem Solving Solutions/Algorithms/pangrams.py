#!/bin/python3

import math
import os
import random
import re
import sys
import operator

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    flag = False
    for i in range(1,27):
        if operator.countOf(s,chr(64+i)) >= 1 or operator.countOf(s,chr(96+i)) >= 1:
            flag = True
        else:
            flag = False
            break
    if flag == True:
        return "pangram"
    else:
        return "not pangram"
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
