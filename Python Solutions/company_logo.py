#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict as dd


if __name__ == '__main__':
    s = input()
    charCount = dd(int)
    newDict,count = dict(), 0
    for i in s:
        charCount[i]+=1
    for key,value in sorted(charCount.items()):
        newDict[key]=value    
    for i in sorted(newDict, key = charCount.get, reverse = True):
        if count <= 2:    
            print(i, charCount[i])
        count+=1