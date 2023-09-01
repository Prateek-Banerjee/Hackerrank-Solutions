from numpy import zeros as z, ones as o

inp = tuple(list(map(int, input().split())))
print(z(inp,dtype=int))
print(o(inp,dtype=int))