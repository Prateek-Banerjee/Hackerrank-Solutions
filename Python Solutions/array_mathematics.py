import numpy

n,m = map(int,input().split())
lomA = []
lomB = []
for i in range(n):
    #elem = list(map(int, input().split()))
    lomA.append(list(map(int, input().split())))

arrA = numpy.array(lomA)
for i in range(n):
    #elem = list(map(int, input().split()))
    lomB.append(list(map(int, input().split())))

arrB = numpy.array(lomB)

print(numpy.add(arrA,arrB))
print(numpy.subtract(arrA,arrB))
print(numpy.multiply(arrA,arrB))
print(numpy.floor_divide(arrA,arrB))
print(numpy.mod(arrA,arrB))
print(numpy.power(arrA,arrB))