n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [float("inf") for _ in range(k + 1)]

for i in range(1, k + 1):
    for c in coins:
        if i == c:
            dp[i] = 1
        if i + c < k + 1:
            dp[i + c] = min(dp[i + c], dp[i] + 1)

ans = dp[-1] if dp[-1] != float("inf") else -1
print(ans)