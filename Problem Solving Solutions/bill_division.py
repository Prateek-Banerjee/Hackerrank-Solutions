#!/bin/python3
#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    # Write your code here
    tot_bill = sum(bill)
    billtobedivided = tot_bill - bill[k] # this is the amount that will be divided equally between Biran and Anna    
    if b == (billtobedivided/2):
        print("Bon Appetit")
    else:
        print(b-(billtobedivided//2))

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1]) # the price of the item that Anna did not eat

    bill = list(map(int, input().rstrip().split()))

    b = int(input()) # amount that Anna should pay as it has been charged by Brian

    bonAppetit(bill, k, b)
