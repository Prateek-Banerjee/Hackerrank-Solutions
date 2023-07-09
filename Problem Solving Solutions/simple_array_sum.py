#!/bin/python3
#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    # Write your code here
    return sum(ar)
if __name__ == '__main__':

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    print(simpleArraySum(ar))
