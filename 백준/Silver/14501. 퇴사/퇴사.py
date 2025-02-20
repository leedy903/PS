N = int(input())

T = [0 for _ in range(N)]
P = [0 for _ in range(N)]
DP = [0 for _ in range(N+1)]

for i in range(N):
    T[i], P[i] = map(int, input().split())

for i in range(N - 1, -1, -1):
    if i + T[i] > N:
        DP[i] = DP[i + 1]
    else:
        DP[i] = max(DP[i + 1], P[i] + DP[i + T[i]])
print(DP[0])