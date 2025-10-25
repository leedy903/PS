from collections import deque
import sys
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
borders = []

continent_id = 0
visited = [[False] * n for _ in range(n)]
for y in range(n):
    for x in range(n):
        if matrix[y][x] == 1 and not visited[y][x]:
            continent_id += 1
            deq = deque([(y, x)])
            visited[y][x] = True
            matrix[y][x] = continent_id
            while deq:
                cy, cx = deq.popleft()
                is_border = False
                for i in range(4):
                    ny, nx = cy + dy[i], cx + dx[i]
                    if 0 <= ny < n and 0 <= nx < n:
                        if not visited[ny][nx] and matrix[ny][nx] == 1:
                            visited[ny][nx] = True
                            matrix[ny][nx] = continent_id
                            deq.append((ny, nx))
                        elif matrix[ny][nx] == 0:
                            is_border = True
                if is_border:
                    borders.append([cy, cx])

deq = deque()
dist = [[-1] * n for _ in range(n)]
for y, x in borders:
    deq.append((y, x))
    dist[y][x] = 0

answer = float('inf')

while deq:
    y, x = deq.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            if matrix[ny][nx] == 0:
                matrix[ny][nx] = matrix[y][x]
                dist[ny][nx] = dist[y][x] + 1
                deq.append((ny, nx))
            elif matrix[ny][nx] != matrix[y][x]:
                answer = min(answer, dist[y][x] + dist[ny][nx])

print(answer)
