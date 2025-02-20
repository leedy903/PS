N = int(input())
M = int(input())
vips = [int(input()) for _ in range(M)]
    
dp = [1, 1, 2]
for i in range(3, N + 1):
    dp.append(dp[i - 1] + dp[i - 2])

ans = 1
pre = 0
for i in range(0, M):
    ans = ans * dp[vips[i] -1 -pre]
    pre = vips[i]
    
ans = ans * dp[N - pre]
print(ans)