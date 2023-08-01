# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations as cmb

n = int(input())
inp = input().split()
k = int(input())

count = 0
for i in list(cmb(inp,k)):
    if 'a' in i:
        count+=1
print("{:.3f}".format(count/len(list(cmb(inp,k)))))