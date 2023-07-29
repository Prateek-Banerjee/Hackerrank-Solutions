# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    n = int(input())
    cnts = set()
    for i in range(n):
        cnt = input()
        cnts.add(cnt)
    print(len(cnts))
        
    