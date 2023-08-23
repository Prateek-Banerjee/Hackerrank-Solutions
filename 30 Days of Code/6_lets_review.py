# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
for i in range(t):
    s = input() 
    evenIndex = oddIndex = ""   
    for i in range(len(s)):
        if i%2 == 0:
            evenIndex+=s[i]
        else:
            oddIndex+=s[i]
    
    print(evenIndex,oddIndex)