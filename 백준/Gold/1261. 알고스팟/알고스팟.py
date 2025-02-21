import sys
from heapq import heappop, heappush
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

m, n = map(int, input().split())
matrix = [list(map(int, list(input()[:-1]))) for _ in range(n)]
dist = [[float("inf") for _ in range(m)] for _ in range(n)]
visit = [[False for _ in range(m)] for _ in range(n)]

dist[0][0] = 0
heap = [[dist[0][0], [0, 0]]]
while heap:
    cost, now = heappop(heap)
    y, x = now
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if not visit[ny][nx]:
                next_cost = cost + matrix[ny][nx]
                if dist[ny][nx] > next_cost:
                    dist[ny][nx] = next_cost
                    visit[ny][nx] = True
                    heappush(heap, [dist[ny][nx], [ny, nx]])

print(dist[-1][-1])