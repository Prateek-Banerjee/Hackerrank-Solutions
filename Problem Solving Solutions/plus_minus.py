#!/bin/python3
#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    cp,cn,cz = 0,0,0
    for i in arr:
        if i > 0:
            cp+=1
        elif i < 0:
            cn += 1
        elif i == 0:
            cz += 1
    print("{:.6f}".format(cp/(len(arr))))
    print("{:.6f}".format(cn/(len(arr))))
    print("{:.6f}".format(cz/(len(arr))))

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
