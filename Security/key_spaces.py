# Enter your code here. Read input from STDIN. Print output to STDOUT
s,e = input(),int(input())
newstr = []
for i in s:
    newstr.append(chr(((ord(i)-48+e)%10)+48))
print("".join(newstr))