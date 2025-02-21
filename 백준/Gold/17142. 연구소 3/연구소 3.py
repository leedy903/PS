from collections import deque

n, m = map(int, input().split())
matrix = [None for _ in range(n)]

virus_position = []
virus = 0
for y in range(n):
    row = list(map(int, input().split()))
    for x in range(n):
        if row[x] == 2:
            virus += 1
            virus_position.append([y, x])
    matrix[y] = row


dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

answer = float("inf")

def dfs(depth, index, start_virus):
    global answer
    if depth == m:
        time = bfs(start_virus)
        answer = min(answer, time)
        return

    for i in range(index, virus):
        if not start_virus[i]:
            start_virus[i] = True
            dfs(depth + 1, i + 1, start_virus)
            start_virus[i] = False


def bfs(start_virus):
    global answer
    dp = [list(float("inf") for _ in range(n)) for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in  range(n)]

    deq = deque([])

    for i in range(virus):
        y, x = virus_position[i]
        dp[y][x] = 0
        if start_virus[i]:
            visited[y][x] = True
            deq.append([y, x])

    while deq:
        y, x = deq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if not visited[ny][nx] and matrix[ny][nx] != 1:
                    dp[ny][nx] = dp[y][x] + 1
                    visited[ny][nx] = True
                    deq.append([ny, nx])
    
    time = 0
    for y in range(n):
        for x in range(n):
            if matrix[y][x] == 0:
                time = max(time, dp[y][x])

    return time


start_virus = [False for _ in range(virus)]
dfs(0, 0, start_virus)
answer = answer if answer != float("inf") else -1
print(answer)