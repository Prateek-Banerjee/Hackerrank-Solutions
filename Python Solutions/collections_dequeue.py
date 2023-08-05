# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque as dq

n = int(input())
dqueue = dq()
for i in range(n):
    comm = input()
    if ((comm.split())[0]).startswith("append") and not(((comm.split())[0]).endswith("left")):
        dqueue.append(int((comm.split())[1]))
    if ((comm.split())[0]).startswith("append") and ((comm.split())[0]).endswith("left"):
        dqueue.appendleft(int((comm.split())[1]))
    if ((comm.split())[0]).startswith("pop") and not(((comm.split())[0]).endswith("left")):
        dqueue.pop()
    if ((comm.split())[0]).startswith("pop") and ((comm.split())[0]).endswith("left"):
        dqueue.popleft()

print(*dqueue)