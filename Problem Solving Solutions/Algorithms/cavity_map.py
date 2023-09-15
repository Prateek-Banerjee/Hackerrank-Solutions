#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#

def cavityMap(grid):
    # Write your code here
    if len(grid)<=2:
        return grid
    else:
        for i in range(len(grid)-1):
            for j in range(len(grid)-1):
                try:
                    if i == 0 or j == 0 or i == len(grid)-1 or j == len(grid)-1:
                        continue
                    else:
                        if (int(grid[i][j]) > int(grid[i-1][j])) and (int(grid[i][j]) > int(grid[i][j-1])) and (int(grid[i][j]) > int(grid[i][j+1])) and (int(grid[i][j]) > int(grid[i+1][j])):
                            grid[i] = grid[i][:j] + 'X' + grid[i][j+1:]                        
                except:
                    continue                        
    return (grid)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
