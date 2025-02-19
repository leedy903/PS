import sys
from collections import deque
input = sys.stdin.readline

n, l, r = map(int, input().split())
matrix = [list(map(int, input().rstrip().split())) for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

days = 0
while True:
    immigration = False
    visited = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                union = [[i, j]]
                visited[i][j] = True
                deq = deque([[i, j]])
                while deq:
                    y, x = deq.popleft()
                    for k in range(4):
                        ny = y + dy[k]
                        nx = x + dx[k]
                        if 0 <= ny < n and 0 <= nx < n:
                            if not visited[ny][nx] and l <= abs(matrix[ny][nx] - matrix[y][x]) <= r: 
                                visited[ny][nx] = True
                                deq.append([ny, nx])
                                union.append([ny, nx])
                
                if len(union) > 1:
                    immigration = True
                    population = sum([matrix[y][x] for y, x in union]) // len(union)
                    for y, x in union:
                        matrix[y][x] = population

    if not immigration:
        break

    days += 1

print(days)