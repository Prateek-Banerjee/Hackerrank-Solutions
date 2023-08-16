# Enter your code here. Read input from STDIN. Print output to STDOUT
num = int(input())
numList = list(map(int, input().split()))

print("YES" if num in numList and all(numList.count(i) == 1 for i in numList) else "NO")