from collections import deque
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]
M, N = map(int, input().split())
matrix = [None for _ in range(N)]
ripen_tomato = deque([])

days = 0
for i in range(N):
    rows = list(map(int, input().split()))
    for j in range(M):
        if rows[j] == 1:
            ripen_tomato.append([i, j])
    matrix[i] = rows

while True:
    unripen_tomato = deque([])
    while ripen_tomato:
        y, x = ripen_tomato.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and matrix[ny][nx] == 0:
                matrix[ny][nx] = 1
                unripen_tomato.append([ny, nx])

    if len(unripen_tomato) == 0:
        break
    days += 1
    ripen_tomato = unripen_tomato

for i in range(N):
    if 0 in matrix[i]:
        days = -1
        break

print(days)


