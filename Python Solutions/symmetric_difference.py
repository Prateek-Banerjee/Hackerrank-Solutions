m = int(input())
a = set(map(int, input().rstrip().split()))
n = int(input())
b = set(map(int, input().rstrip().split()))

for i in sorted((a.difference(b)).union(b.difference(a))):
    print (i)