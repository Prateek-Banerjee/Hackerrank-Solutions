if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        numA = int(input())
        elemA = set(map(int, input().split()))
        numB = int(input())
        elemB = set(map(int, input().split()))
        if len(elemA.intersection(elemB)) == len(elemA): print (True)
        else: print (False)
"""OR

if __name__ == "__main__":
   t = int(input())
   for i in range(t):
       numA = int(input())
       elemA = set(map(int, input().split()))
       numB = int(input())
       elemB = set(map(int, input().split()))
       print(elemA.issubset(elemB))"""