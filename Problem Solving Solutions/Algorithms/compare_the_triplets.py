#!/bin/python3
#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    c = [0,0]
    for i in range(3):
        if a[i] > b[i]: c[0]+=1
        elif a[i] < b[i]: c[1]+=1
    print(c[0],c[1])

if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    compareTriplets(a, b)
