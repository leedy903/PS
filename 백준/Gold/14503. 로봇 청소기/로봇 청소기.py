import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

n, m = map(int, input().rstrip().split())
y, x, d = map(int, input().rstrip().split())
matrix = [list(map(int, input().rstrip().split())) for _ in range(n)]

matrix[y][x] = 2
deq = deque([[y, x, d]])
ans = 1
count = 0
while deq:
    y, x, d = deq.popleft()

    dirty_area = [False for _ in range(4)]
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < m and matrix[ny][nx] == 0:
            dirty_area[i] = True
        else:
            dirty_area[i] = False
    
    if not any(dirty_area):
        nd = (d + 2) % 4
        ny = y + dy[nd]
        nx = x + dx[nd]
        if 0 <= ny < n and 0 <= nx < m and matrix[ny][nx] != 1:
            deq.append([ny, nx, d])
        else:
            break

    for i in range(4):
        nd = (d - (i + 1)) % 4
        if dirty_area[nd]:
            ny = y + dy[nd]
            nx = x + dx[nd]
            matrix[ny][nx] = 2
            deq.append([ny, nx, nd])
            ans += 1
            break
    count += 1
    
print(ans)