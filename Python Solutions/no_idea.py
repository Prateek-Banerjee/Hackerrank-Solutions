first_mult_input = input().rstrip().split()
n,m = first_mult_input[0],first_mult_input[1]

arr = list(map(int, input().rstrip().split()))
a = set(map(int, input().rstrip().split()))
b = set(map(int, input().rstrip().split()))

happiness = 0

for i in arr:
    if i in a and i not in b: happiness+=1
    elif i in b and i not in a: happiness-=1

print(happiness)