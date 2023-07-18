if __name__ == '__main__':
    N = int(input())
    l = []
    for i in range(N):
        comm = input()
        if comm.startswith("insert"):
            l.insert(int((comm.split())[1]), int((comm.split())[2]))
        if comm.startswith("print"):
            print(l)
        if comm.startswith("remove"):
            l.remove(int((comm.split())[1]))
        if comm.startswith("append"):
            l.append(int((comm.split())[1]))
        if comm.startswith("sort"):
            l.sort()
        if comm.startswith("pop"):
            l.pop()
        if comm.startswith("reverse"):
            l.reverse()