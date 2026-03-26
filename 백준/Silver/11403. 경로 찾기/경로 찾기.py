import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
adj_matrix = [list(map(int, input().strip().split())) for _ in range(N)]

reachable = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    visited = [0] * N
    deq = deque([i])

    while deq:
        cur = deq.popleft()
        for next in range(N):
            if adj_matrix[cur][next] == 1 and not visited[next]:
                visited[next] = 1
                deq.append(next)
    
    for j in range(N):
        reachable[i][j] = visited[j]
    
for i in range(N):
    print(*reachable[i])