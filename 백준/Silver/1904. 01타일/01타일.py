N = int(input())
DP = [1 for _ in range(N+2)]
for i in range(2, N+1):
    DP[i] = (DP[i-1] + DP[i-2])%15746
print(DP[N])