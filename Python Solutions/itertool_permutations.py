from itertools import permutations as per

inp = input().split()
l = sorted(list(per(inp[0],int(inp[1]))))
for i in l:
    print("".join(i))