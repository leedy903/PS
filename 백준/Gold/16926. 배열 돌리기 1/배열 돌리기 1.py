import sys
from collections import deque
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

n, m, r = map(int, input().split())
matrix = [list(map(int, input().rstrip().split())) for _ in range(n)]

depth = min(n, m) // 2
for d in range(depth):
    deq = deque()
    y, x = d, d
    for i in range(4):
        while True:
            ny = y + dy[i]
            nx = x + dx[i]
            if d <= ny < n - d and d <= nx < m - d:
                deq.append(matrix[ny][nx])
                y, x = ny, nx
            else:
                break
            
    deq.rotate(-r % ((n + m - 4 * d) * 2 - 4))
    
    y, x = d, d
    for i in range(4):
        while True:
            ny = y + dy[i]
            nx = x + dx[i]
            if d <= ny < n - d and d <= nx < m - d:
                matrix[ny][nx] = deq.popleft()
                y, x = ny, nx
            else:
                break

for row in matrix:
    print(*row)