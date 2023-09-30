import numpy


poly = list(map(float, input().split()))
x = int(input())

print(numpy.polyval(poly, x))