from itertools import combinations as cmb

inp = input().split()
for j in range(1,int(inp[1])+1):
    for i in list(cmb("".join(sorted(inp[0])),j)):
        print("".join(i))