#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'theLoveLetterMystery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def theLoveLetterMystery(s):
    # Write your code here
    nop = 0
    if len(s) == 1:
        return nop
    elif s == s[::-1]:
        return nop
    else:
        if len(s)%2 == 0:
            fhf=s[0:(len(s)//2)]
            shf=s[(len(s)//2):]
            for i in range(len(fhf)):
                if fhf[i] != shf[-1-i]:
                    if ord((shf[-1-i]))>ord((fhf[i])):
                        nop = nop + (ord((shf[-1-i]))-ord((fhf[i])))
                    elif ord((shf[-1-i]))<ord((fhf[i])):
                        nop = nop + (ord((fhf[i]))-ord((shf[-1-i])))
        else:
            fhf=s[0:(len(s)//2)]
            shf=s[(len(s)//2)+1:]
            for i in range(len(fhf)):
                if shf[-1] == 'a' and fhf[0] == 'z':
                    nop = nop+26
                elif fhf[i] != shf[-1-i]:
                    if ord((shf[-1-i]))>ord((fhf[i])):
                        nop = nop + (ord((shf[-1-i]))-ord((fhf[i])))
                    elif ord((shf[-1-i]))<ord((fhf[i])):
                        nop = nop + (ord((fhf[i]))-ord((shf[-1-i])))
        return nop    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
