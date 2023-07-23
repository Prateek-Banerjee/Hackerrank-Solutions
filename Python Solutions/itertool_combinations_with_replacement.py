from itertools import combinations_with_replacement as cmb

inp = input().split()
for i in list(cmb(sorted(inp[0]),int(inp[1]))):
    print("".join(i))