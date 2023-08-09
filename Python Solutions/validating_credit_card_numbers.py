# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
n = int(input())
allowed = "0123456789-"
for i in range(n):
    ccnum = input()
    if ccnum.count('-')>0:
        justnum = list(filter(lambda char: char != '-', ccnum.replace('-', '', 3)))
        if int(ccnum[0]) not in [4,5,6] or any(i not in allowed for i in ccnum) or any(sum(1 for _ in group) > 3 for _, group in itertools.groupby(justnum) if _ == _) or any(len(i)!=4 for i in (ccnum.split('-'))) or len(justnum) != 16:
            print ("Invalid")
        else: print("Valid")
    elif int(ccnum[0]) not in [4,5,6] or any(i not in allowed for i in ccnum) or any(sum(1 for _ in group) > 3 for _, group in itertools.groupby(ccnum) if _ == _) or len(ccnum) != 16:
        print ("Invalid")
    else:
        print ("Valid")
    