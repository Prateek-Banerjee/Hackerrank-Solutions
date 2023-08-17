# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())

for i in range(n):
    s = input()
    s = (re.sub(r"(?<=\s)&&(?=\s)","and",s))
    s = (re.sub(r"(?<=\s)\|{2}(?=\s)","or",s))
    print(s)