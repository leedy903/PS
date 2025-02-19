import sys
from  collections import deque
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

n, m = map(int, input().rstrip().split())
matrix = [list(map(int, list(input().rstrip()))) for _ in range(n)]
route = [[float('inf') for _ in range(m)] for _ in range(n)]

deq = deque([[0, 0]])
route[0][0] = 1
while deq:
    y, x = deq.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if matrix[ny][nx] == 1 and route[ny][nx] > route[y][x] + 1:
                route[ny][nx] = route[y][x] + 1
                deq.append([ny, nx])

print(route[-1][-1])