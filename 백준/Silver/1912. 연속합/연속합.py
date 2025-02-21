n = int(input())

sequence = list(map(int, input().split()))
dp = [0 for _ in range(n + 1)]

dp[0] = 0
for i in range(1, n + 1):
    dp[i] = max(dp[i - 1], 0) + sequence[i - 1]

print(max(dp[1:]))