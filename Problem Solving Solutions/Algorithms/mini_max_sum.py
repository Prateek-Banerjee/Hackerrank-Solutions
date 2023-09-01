#!/bin/python3
#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
def miniMaxSum(arr):
    # Write your code here
    minsum,maxsum = 0,0
    for i in range(len(arr)):
        if i < len(arr)-1:
            minsum+=arr[i]
        if i > 0:
            maxsum+=arr[i]
    print(minsum, maxsum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))
    arr.sort()
    miniMaxSum(arr)
