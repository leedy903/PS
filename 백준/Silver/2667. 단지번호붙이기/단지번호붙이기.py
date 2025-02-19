N = int(input())
MAP = [[] for _ in range(N)]
VISITED = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    MAP[i] = list(map(int, list(input())))

numlist = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, num):
    VISITED[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if VISITED[nx][ny] == 0 and MAP[nx][ny] == 1:
                num = dfs(nx, ny, num + 1)
    return num

for i in range(N):
    for j in range(N):
        if MAP[i][j] == 1 and VISITED[i][j] == 0:
            numlist.append(dfs(i, j, 1))

print(len(numlist))
for ans in sorted(numlist):
    print(ans)
