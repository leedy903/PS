import sys
from collections import deque
input = sys.stdin.readline

n, m, r = map(int, input().strip().split())
matrix = [list(map(int, input().strip().split())) for _ in range(n)]

depth = min(n, m) // 2
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

for d in range(depth):
    y, x = d, d
    N = n - d * 2
    M = m - d * 2
    deq = deque()
    for i in range(4):
        while True:
            ny = y + dy[i]
            nx = x + dx[i]
            if d <= ny < d + N and d <= nx < d + M:
                deq.append(matrix[ny][nx])
                y = ny
                x = nx
            else:
                break
    
    rotation = r % ((N - 1) * 2 + (M - 1) * 2)
    deq.rotate(-rotation)

    for i in range(4):
        while True:
            ny = y + dy[i]
            nx = x + dx[i]
            if d <= ny < d + N and d <= nx < d + M:
                matrix[ny][nx] = deq.popleft()
                y = ny
                x = nx
            else:
                break

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=" ")
    print()