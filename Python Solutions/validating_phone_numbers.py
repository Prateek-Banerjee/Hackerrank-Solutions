# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
lnum = list()

for i in range(1,n+1):
    num = input()
    if (num.startswith("7") or num.startswith("8") or num.startswith("9")) and len(num) == 10 and num.isnumeric() == True:
        print("YES")
    else:
        print("NO")
