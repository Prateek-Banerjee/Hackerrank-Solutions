#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gemstones' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY arr as parameter.
#
"""
The below logic is that, in order to check if a mineral is a gemstone or not, the mineral must be present in all the rocks
and here, each mineral is a lowercase character [a-z], and each rock is represented as a string, and we are given a list of 
strings, or in other words, a list of rocks. 

So here, if we check for the fact that, all the distinct characters (aka minerals) of just the first string (aka rock) from the 
list of strings (aka list of rocks) is present in all the other strings (aka all the other rocks) from the list of strings (aka list of rocks)
then that would be a gemstone.

The individualCount is for checking, whether each distint character of the first string is present in all of the other strings 
amongst the list of strings. So, if it is present in all of the other strings, then value of individualCount should be equal to
len(arr)-1 (as the presence of that particular character is checked from index 1 till the end of the list of strings), so we add
1 to the mainCount by doing the following the operation individualCount//len(arr[1:]). The individualCount is set to 0 before checking
the presence of a particular distinct character from the first string in the list of strings.

In case any distinct character of the first string is not found in any of the other intermediate strings from the list of strings, then
we break out of the loop as it does not make sense to check further. 

Finally the mainCount is returned as an output.
"""


def gemstones(arr):
    # Write your code here
    individualCount = mainCount = 0
    for i in set(
        arr[0]
    ):  # to iterate over the distinct characters (aka minerals) of just the first string (aka rock)
        individualCount = 0
        for j in arr[1:]:
            if i in j:
                individualCount += 1
                continue
            else:
                break
        mainCount += individualCount // len(arr[1:])
    return mainCount


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + "\n")

    fptr.close()
