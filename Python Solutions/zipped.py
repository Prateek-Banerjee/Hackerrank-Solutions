# Enter your code here. Read input from STDIN. Print output to STDOUT

n,x = map(int, input().split())
blist = list()
for i in range(x):
    l = list(map(float, input().split()))    
    blist.append(l)

for zlist in list(zip(*blist)):
    print("{:.01f}".format(sum(zlist)/x))
