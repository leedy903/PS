import sys
from collections import defaultdict
from heapq import heappush, heappop

input = sys.stdin.readline

N, M = map(int, input().split())

parents = [i for i in range(N + 1)]

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b
    return

edgeHeap = []

for i in range(M):
    a, b, c = map(int, input().split())
    heappush(edgeHeap, [c, a, b])

edgeCount = 0
lastEdge = 0
cost = 0
while edgeHeap:
    w, u, v = heappop(edgeHeap)

    u = find(u)
    v = find(v)
    if u != v:
        union(u, v)
        cost += w
        edgeCount += 1
        lastEdge = w
    
    if edgeCount == N - 1:
        break

print(cost - lastEdge)