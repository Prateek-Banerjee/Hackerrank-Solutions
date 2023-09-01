import numpy
numpy.set_printoptions(legacy = '1.13')

row,column = map(int,input().split())

print(numpy.eye(row,column))