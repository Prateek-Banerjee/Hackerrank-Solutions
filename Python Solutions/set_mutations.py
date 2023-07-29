# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    n = int(input())
    orset = set(map(int, input().split()))
    onum = int(input())
    for i in range(onum):
        comm = input()
        otset = set(map(int, input().split()))
        if comm.startswith("intersection_update"): orset.intersection_update(otset)
        if comm.startswith("update"): orset.update(otset)
        if comm.startswith("difference_update"): orset.difference_update(otset)
        if comm.startswith("symmetric_difference_update"): orset.symmetric_difference_update(otset)
    
    print(sum(orset))
        