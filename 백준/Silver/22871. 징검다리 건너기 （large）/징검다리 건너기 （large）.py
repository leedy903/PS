import sys
input = sys.stdin.readline

n = int(input())
stones = list(map(int, input().split()))
dp = [float("inf") for _ in range(n)]
dp[0] = 0

for i in range(1, n):
    for j in range(i - 1, -1, -1):
        cost = max(dp[j], (i - j) * (1 + abs(stones[i] - stones[j])))
        dp[i] = min(dp[i], cost)

print(dp[-1])