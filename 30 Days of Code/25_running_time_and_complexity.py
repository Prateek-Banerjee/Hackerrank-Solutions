# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
testCases = int(input())
for t in range(testCases):
    n = int(input())
    if n > 1:
        flag = True
        for i in range(2,(math.ceil(math.sqrt(n)))+1):
            if n>2 and n%i == 0: 
                flag = False
                break
        if flag == True:
            print("Prime")
        else:
            print("Not prime")
    else:
        print("Not prime")