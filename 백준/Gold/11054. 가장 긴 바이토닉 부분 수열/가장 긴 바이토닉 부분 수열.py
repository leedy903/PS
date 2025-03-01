n = int(input())
sequence = list(map(int, input().split()))
dp_ascent = [0 for _ in range(n)]
dp_descent = [0 for _ in range(n)]
dp = [0 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if sequence[j] < sequence[i] and dp_ascent[j] > dp_ascent[i]:
            dp_ascent[i] = dp_ascent[j]
    dp_ascent[i] += 1

sequence.reverse()
for i in range(n):
    for j in range(i):
        if sequence[j] < sequence[i] and dp_descent[j] > dp_descent[i]:
            dp_descent[i] = dp_descent[j]
    dp_descent[i] += 1
dp_descent.reverse()

for i in range(n):
    dp[i] = dp_ascent[i] + dp_descent[i]

print(max(dp) - 1)