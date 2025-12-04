import sys
from heapq import heappush, heappop
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

V, E = map(int, input().split())

parent = list(range(V + 1))
edgeList = []

for i in range(E):
    u, v, w = map(int, input().split())
    heappush(edgeList, [w, u, v])

edgeCount = 0
treeWeight = 0
while len(edgeList) != 0:
    w, u, v = heappop(edgeList)
    u = find(u)
    v = find(v)
    if u != v:
        union(u, v)
        treeWeight += w
        edgeCount += 1
    if edgeCount == V - 1:
        break

print(treeWeight)