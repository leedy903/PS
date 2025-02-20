import sys
sys.setrecursionlimit(10000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    VISITED[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if MATRIX[nx][ny] and not VISITED[nx][ny]:
               dfs(nx, ny)

T = int(input())
for t in range(T):
    cnt = 0
    M, N, K = map(int, input().split())

    MATRIX = [[0 for _ in range(N)] for _ in range(M)]
    VISITED = [[0 for _ in range(N)] for _ in range(M)]

    for i in range(K):
        X, Y = map(int, input().split())
        MATRIX[X][Y] = 1
    
    for i in range(M):
        for j in range(N):
            if MATRIX[i][j] and not VISITED[i][j]:
                dfs(i, j)
                cnt += 1
    print(cnt)