# Enter your code here. Read input from STDIN. Print output to STDOUT
num = int(input())
numSet = list(map(int, input().split()))
for i in range(num):
    print(numSet[numSet[i]-1])