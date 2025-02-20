n = int(input())
sequence = list(map(int, input().split()))
dp = [0 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if sequence[j] < sequence[i] and dp[j] > dp[i]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))