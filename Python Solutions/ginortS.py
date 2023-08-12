# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()
lcCheck = sorted(list(filter(lambda x: 97 <= ord(x) <= 122,s)))
ucCheck = sorted(list(filter(lambda x: 65 <= ord(x) <= 90, s)))
oddDigitCheck = sorted(list(filter(lambda x: 48 <= ord(x) <= 57 and int(x)%2!=0, s)))
evenDigitCheck = sorted(list(filter(lambda x: 48 <= ord(x) <= 57 and int(x)%2==0, s)))

print("".join(lcCheck+ucCheck+oddDigitCheck+evenDigitCheck))