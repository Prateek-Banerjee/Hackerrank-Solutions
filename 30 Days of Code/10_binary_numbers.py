#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    binary_n = bin(n)[2:]
    print(max([len(count1) for count1 in binary_n.split('0')]))