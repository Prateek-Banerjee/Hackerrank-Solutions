n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    comm = input()
    if comm.startswith("pop"): s.pop()
    if comm.startswith("remove"): s.remove(int((comm.split())[1]))
    if comm.startswith("discard"): s.discard(int((comm.split())[1]))

print(sum(s))