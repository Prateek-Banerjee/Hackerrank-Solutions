import numpy

n = int(input())
arr = []
for i in range(n):
    elem = list(map(float, input().split()))
    arr.append(elem)
    
print (round((numpy.linalg.det(numpy.array(arr))),2))