import numpy

n = int(input())

arr1 = numpy.array([list( map( int, input().rstrip().split() )) for _ in range(n)], int)
arr2 = numpy.array([list( map( int, input().rstrip().split() )) for _ in range(n)], int)
print(numpy.dot(arr1,arr2))