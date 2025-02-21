N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
visit = [[False for _ in range(M)] for _ in  range(N)]
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]
max_score = 0
max_point = max(map(max, matrix))

def dfs(y, x, depth, score):
    global max_score
    if max_score >= score + max_point * (4 - depth):
        return

    if depth == 4:
        max_score = max(score, max_score)
        return

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < M and not visit[ny][nx]:
            if depth == 2:
                visit[ny][nx] = True
                dfs(y, x, depth + 1, score + matrix[ny][nx])
                visit[ny][nx] = False
            visit[ny][nx] = True
            dfs(ny, nx, depth + 1, score + matrix[ny][nx])
            visit[ny][nx] = False

for y in range(N):
    for x in range(M):
        visit[y][x] = True
        dfs(y, x, 1, matrix[y][x])
        visit[y][x] = False

print(max_score)
