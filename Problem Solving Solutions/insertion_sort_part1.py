arr = list(map(int, input().rstrip().split()))
n = len(arr)
lastElem = arr[n-1]
for i in range(n-2,-1,-1):
    if arr[i] > lastElem:
        arr [i+1] = arr[i]
    elif arr[i] < lastElem:
        arr [i+1] = lastElem
        break
    print(*arr)
else:
    arr[0] = lastElem
print(*arr)