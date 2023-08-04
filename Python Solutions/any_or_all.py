# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
num = list(map(int, input().split()))
"""if all(i>0 for i in num) and any(str(i)==((str(i))[::-1]) for i in num): 
    print (True)
else:
    print (False)"""
print(all(i>0 for i in num) and any(str(i)==((str(i))[::-1]) for i in num))