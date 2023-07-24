#!/bin/python3
#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    cv,c = 0,0    
    for i in range(steps):
        if path[i] == 'U': c+=1
        elif path[i] == 'D': c-=1
        if path[i]=='U' and c==0: cv+=1
    print(cv)

if __name__ == '__main__':

    steps = int(input())

    path = input()

    result = countingValleys(steps, path)