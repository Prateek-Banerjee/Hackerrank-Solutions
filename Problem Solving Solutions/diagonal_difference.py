#!/bin/python3
#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    sld,srd = 0,0
    for i in range(len(arr)):        
        sld += arr[i][i]
        srd += arr[i][n-1-i]
    print(abs(sld-srd))

if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
        """rows = []
        for __ in range(n):
            rows.append(int(input()))
        arr.append(rows)"""
    result = diagonalDifference(arr)