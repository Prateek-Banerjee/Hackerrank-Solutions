# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = map(int, input().split())
a,b = list(),list()
for i in range(n):
    a.append(input())
for i in range(m):
    b.append(input())

for i in range(m):
    if b[i] in a:
        for j in range(n):
            if a[j] == b[i]:
                print(j+1, end = " ")
        print()
    else:
        print("-1")