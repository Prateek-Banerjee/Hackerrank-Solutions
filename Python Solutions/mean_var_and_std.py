import numpy



n,m = map(int, input().split())
interimArray = []
for i in range(n):
    interimArrayElements = list(map(int, input().split()))
    interimArray.append(interimArrayElements)

finalArray = numpy.array(interimArray)
print (numpy.mean(finalArray, axis=1),numpy.var(finalArray, axis=0),round((numpy.std(finalArray, axis=None)),11),sep="\n")