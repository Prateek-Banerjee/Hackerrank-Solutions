#!/bin/python3
#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    min,max,cmin,cmax = scores[0],scores[0],0,0
    for i in range(1,len(scores)):
        if scores[i] < min: 
            min = scores[i]
            cmin+=1
        elif scores[i] > max: 
            max = scores[i]
            cmax+=1
    print (cmin,cmax)
if __name__ == '__main__':
    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
