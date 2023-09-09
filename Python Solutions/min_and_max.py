import numpy



n,m = map(int, input().split())
interimArray = []
for i in range(n):
    interimArrayElements = list(map(int, input().split()))
    interimArray.append(interimArrayElements)

finalArray = numpy.array(interimArray)
print (numpy.max(numpy.min(finalArray,axis=1)))