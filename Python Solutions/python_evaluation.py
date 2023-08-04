# Enter your code here. Read input from STDIN. Print output to STDOUT
text = input()
if "print" not in text:
    print (eval(text))
else:
    eval(text)