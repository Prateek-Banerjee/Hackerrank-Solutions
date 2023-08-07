import numpy

"""arr = list(map(int, input().split()))
print(numpy.reshape(arr,(3,3)))"""

arr = numpy.array(list(map(int, input().split())))
arr.shape = (3,3)
print(arr)