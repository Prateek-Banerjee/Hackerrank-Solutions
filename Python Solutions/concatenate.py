import numpy

n,m,p = map(int, input().split())
arr_1 = list()
arr_2 = list()
for i in range(n):
    elem = list(map(int, input().split()))
    arr_1.append(elem)
for i in range(m):
    elem = list(map(int, input().split()))
    arr_2.append(elem)
 
final_arr_1 = numpy.array(arr_1)
final_arr_2 = numpy.array(arr_2)
print (numpy.concatenate((final_arr_1, final_arr_2), axis = 0))