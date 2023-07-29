if __name__ == "__main__":
    orgset = set(map(int, input().split()))
    t = int(input())
    flag = 0
    for i in range(t):
        otrset = set(map(int, input().split()))       
        if orgset.issuperset(otrset) == True: continue
        else: flag+=1

    if flag == 0: print(True)
    else: print(False)