# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()
newstr = []
for i in s:
    newstr.append(chr(((ord(i)-48+1)%10)+48))
print("".join(newstr))