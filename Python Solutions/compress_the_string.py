# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()
count = 1
for i in range(len(s)):
    if i<len(s)-1:
        if s[i+1] == s[i]:
            count+=1
            continue
        else:
            print("({}, {})".format(count,(s[i])), end=" ")
            count = 1
    else:
        print("({}, {})".format(count,(s[i])), end=" ")
            