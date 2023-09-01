import numpy

n, m = map(int, input().split())
elems = []
for i in range(n):
    arr = list(map(int, input().split()))
    elems.append(arr)

print(numpy.prod(numpy.sum(elems, axis = 0)))
    
    