import sys
input = sys.stdin.readline

MAX_COST = float("inf")
c, n = map(int, input().split())
city_info = [list(map(int, input().split())) for _ in range(n)]
dp = [float("inf") for _ in range(c + 100)]
dp[0] = 0

for cost, client in city_info:
    for i in range(client, c + 100):
        dp[i] = min(dp[i - client] + cost, dp[i])

print(min(dp[c:]))