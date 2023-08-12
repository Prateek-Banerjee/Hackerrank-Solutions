# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product as pc

k, m = map(int, input().split())
listOfLists, val = list(), list()
for i in range(k):
    listOfLists.append((list(map(int, input().split())))[1::])

"""
The product module aliased as pc, when applied on the listOfLists provides all the possible combinations of the
different elements from each of the lists from the listOfLists. Each such combination is a tuple and the combinations
is a list of such tuples.
"""

combinations = list(pc(*listOfLists))
for j in combinations:
    indVal = 0
    for x in j:
        indVal += x * x
    val.append(indVal % m)
print(max(val))
