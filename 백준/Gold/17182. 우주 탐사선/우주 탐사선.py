import sys
input = sys.stdin.readline

def dfs(depth, cur, cost):
    global answer

    if depth == N:
        answer = min(answer, cost)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i, cost + cost_matrix[cur][i])
            visited[i] = False

N, K = map(int, input().split())
cost_matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [False for _ in range(N)]

answer = float('inf')

for k in range(N):
    for i in range(N):
        for j in range(N):
            cost_matrix[i][j] = min(cost_matrix[i][j], cost_matrix[i][k] + cost_matrix[k][j])

answer = float('inf')
dfs(0, K, 0)

print(answer)