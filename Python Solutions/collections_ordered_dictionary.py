# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict as ordic

n = int(input())
ordered_dictionary = ordic()
for i in range(n):
    *name,price = input().split()
    name = " ".join(name)
    if name not in ordered_dictionary.keys():
        ordered_dictionary[name] = int(price)
    else:
        ordered_dictionary[name] += int(price)

for nm,cost in ordered_dictionary.items():
    print(nm,cost)