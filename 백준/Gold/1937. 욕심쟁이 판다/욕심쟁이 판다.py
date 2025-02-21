import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

n = int(input())
matrix = [list(map(int, input().strip().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

def dfs(y, x):
    if dp[y][x] != 0:
        return dp[y][x]
    dp[y][x] = 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            if matrix[y][x] < matrix[ny][nx]:
                dp[y][x] = max(dp[y][x], dfs(ny, nx) + 1)
    
    return dp[y][x]

for y in range(n):
    for x in range(n):
        dp[y][x] = max(dp[y][x], dfs(y, x))

print(max(map(max, dp)))