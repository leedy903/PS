n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0 for _ in range(m)] for _ in range(n + 1)] for _ in range(3)]

ans = float('inf')

for i in range(1, n + 1):
    for j in range(m):
        if j == 0:
            dp[0][i][j] = min(dp[1][i - 1][j], dp[2][i - 1][j + 1]) + matrix[i - 1][j]
            dp[1][i][j] = dp[2][i - 1][j + 1] + matrix[i - 1][j]
            dp[2][i][j] = dp[1][i - 1][j] + matrix[i - 1][j]
        elif j == m - 1:
            dp[0][i][j] = dp[1][i - 1][j] + matrix[i - 1][j]
            dp[1][i][j] = dp[0][i - 1][j - 1] + matrix[i - 1][j]
            dp[2][i][j] = min(dp[0][i - 1][j - 1], dp[1][i - 1][j]) + matrix[i - 1][j]
        else:
            dp[0][i][j] = min(dp[1][i - 1][j], dp[2][i - 1][j + 1]) + matrix[i - 1][j]
            dp[1][i][j] = min(dp[0][i - 1][j - 1], dp[2][i - 1][j + 1]) + matrix[i - 1][j]
            dp[2][i][j] = min(dp[0][i - 1][j - 1], dp[1][i - 1][j]) + matrix[i - 1][j]

for j in range(m):
    ans = min(dp[0][n][j], dp[1][n][j], dp[2][n][j], ans)

print(ans)