#!/bin/python3
#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    # Write your code here
    f=1
    while n!=0:
        f*=n
        n-=1
    print(f)

if __name__ == '__main__':
    n = int(input())
    extraLongFactorials(n)
