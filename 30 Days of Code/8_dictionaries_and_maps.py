# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
phonebook = dict()
for i in range(n):
    name, phone = input().split()
    if name not in phonebook.keys():
        phonebook[name] = int(phone)

while True:
    try:
        nameCheck = input()
        if nameCheck in phonebook.keys():
            print(nameCheck,"=",phonebook[nameCheck],sep="")
        else:
            print("Not found")
    except EOFError:
        break