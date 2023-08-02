#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    count = 0
    spChar = "!@#$%^&*()-+"
    #for i in password:
    if any(i.islower() for i in password) == False: count+=1
    if any(i.isupper() for i in password) == False: count+=1
    if any(i.isdigit() for i in password) == False: count+=1
    if any(i in spChar for i in password) == False: count+=1
    if n>=6 or n+count>=6: return count
    else: return (6-n)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
