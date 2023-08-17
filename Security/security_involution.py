# Enter your code here. Read input from STDIN. Print output to STDOUT
num = int(input())
numSet = list(map(int, input().split()))
count = 0
for i in range(1,num+1):
    if (numSet[i-1]) == (numSet.index(i)+1):
        count+=1
        continue
    else:
        print("NO")
        break
if count == num:
    print("YES")
