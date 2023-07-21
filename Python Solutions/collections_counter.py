# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

x = int(input())
avss = list(map(int, input().rstrip().split()))
avssc = dict((Counter(avss)))
n = int(input())
price=0
for i in range(n):
    dssp = list(map(int, input().rstrip().split()))
    if dssp[0] in avssc.keys() and avssc[dssp[0]]!=0:
        price+=dssp[1]
        avssc[dssp[0]]-=1
print(price)