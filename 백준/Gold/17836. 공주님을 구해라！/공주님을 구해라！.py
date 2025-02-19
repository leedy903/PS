import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

n, m, t = map(int, input().split())
matrix = [list(map(int, input().rstrip().split())) for _ in range(n)]
route = [[float('inf') for _ in range(m)] for _ in range(n)]

deq = deque([[0, 0]])
route[0][0] = 0
while deq:
    y, x = deq.popleft()
    
    if matrix[y][x] == 2:
        route[-1][-1] = min(route[-1][-1], route[y][x] + (n - y - 1) + (m - x - 1))
        continue
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        
        if 0 <= nx < m and 0 <= ny < n:
            if matrix[ny][nx] != 1 and route[ny][nx] > route[y][x] + 1:
                route[ny][nx] = route[y][x] + 1
                deq.append([ny, nx])

ans = "Fail" if route[-1][-1] > t else route[-1][-1]
print(ans)