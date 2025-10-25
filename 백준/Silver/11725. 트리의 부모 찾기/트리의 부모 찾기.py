import sys
from collections import defaultdict
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = defaultdict(list)
for i in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

parents = [0 for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
deq = deque([1])
visited[1] = True
while deq:
    cur = deq.popleft()
    visited[cur] = True
    for child in graph[cur]:
        if not (visited[child]):
            parents[child] = cur
            deq.append(child)
    
for i in range(2, n + 1):
    print(parents[i])