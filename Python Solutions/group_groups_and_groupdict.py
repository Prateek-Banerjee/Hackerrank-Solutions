# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
s = input()

for j,group in itertools.groupby(s):
    if j==j and j.isalnum():
        if sum(1 for j in group)>1:
            print(j)
            break
        else:
            continue
else:
     print("-1")