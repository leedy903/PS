import sys
from collections import deque
input = sys.stdin.readline


dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [list(False for _ in range(m)) for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0 and not visited[i][j]:
            ans += 1
            visited[i][j] = True
            deq = deque([[i, j]])
            while deq:
                y, x = deq.popleft()
                for d in range(4):
                    ny = (y + dy[d]) % n
                    nx = (x + dx[d]) % m
                    if matrix[ny][nx] == 0 and not visited[ny][nx]:
                        visited[ny][nx] = True
                        deq.append([ny, nx])

print(ans)