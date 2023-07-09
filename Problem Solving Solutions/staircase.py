#!/bin/python3
#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
def staircase(n):
    # Write your code here
    k= 1
    for i in range(n,0,-1):
        for j in range(i-1):
            print(" ",end="")
        print("#"*k)        
        k+=1
if __name__ == '__main__':
    n = int(input())
     
    staircase(n)       
