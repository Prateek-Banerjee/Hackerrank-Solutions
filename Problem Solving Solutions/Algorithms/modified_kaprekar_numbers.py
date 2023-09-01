#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#


def kaprekarNumbers(p, q):
    # Write your code here
    allKaprekarNumbers = list()
    for i in range(p, q + 1):
        sq = str(i * i)
        lhalf, rhalf = sq[: (len(sq) - len(str(i)))], sq[-len(str(i)) :]
        if lhalf != "" and rhalf != "":
            if int(lhalf) + int(rhalf) == i:
                allKaprekarNumbers.append(i)
        elif lhalf != "" and rhalf == "":
            if int(lhalf) + 0 == i:
                allKaprekarNumbers.append(i)
        elif lhalf == "" and rhalf != "":
            if 0 + int(rhalf) == i:
                allKaprekarNumbers.append(i)

    if len(allKaprekarNumbers) > 0:
        print(*allKaprekarNumbers)
    else:
        print("INVALID RANGE")


if __name__ == "__main__":
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
