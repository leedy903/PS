from collections import deque

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

max_safe_zone = 1
max_height = max(map(max, matrix))
for _ in range(1, max_height):
    for y in range(N):
        for x in range(N):
            matrix[y][x] = max(0, matrix[y][x] - 1)

    safe_zone_count = 0
    visit = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if matrix[i][j] != 0 and not visit[i][j]:
                safe_zone_count += 1
                deq = deque([[i, j]])
                visit[i][j] = True
                while deq:
                    y, x = deq.popleft()
                    for k in range(4):
                        ny = y + dy[k]
                        nx = x + dx[k]
                        if 0 <= ny < N and 0 <= nx < N:
                            if not visit[ny][nx] and matrix[ny][nx] != 0:
                                visit[ny][nx] = True
                                deq.append([ny, nx])

    max_safe_zone = max(max_safe_zone, safe_zone_count)

print(max_safe_zone)