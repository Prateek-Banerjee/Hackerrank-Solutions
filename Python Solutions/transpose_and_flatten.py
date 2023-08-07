import numpy

n,m = map(int,input().split())
arr = list()
for i in range(n):
    l = list(map(int, input().split()))
    arr.append(l)
    
print((numpy.transpose(arr)))
print((numpy.array(arr)).flatten())