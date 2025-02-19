import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

visit = [False for _ in range(N)]

connections = {}

for i in range(N):
    connections[i] = []

for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    
    connections[u - 1].append(v - 1)
    connections[v - 1].append(u - 1)

network_num = 0
for node in connections.keys():
    if visit[node]:
        continue

    visit[node] = True
    network_num += 1

    deq = deque()
    deq.append(node)

    while deq:
        current_node = deq.popleft()
        for adj_node in connections[current_node]:
            if not visit[adj_node]:
                visit[adj_node] = True
                deq.append(adj_node)

print(network_num)
