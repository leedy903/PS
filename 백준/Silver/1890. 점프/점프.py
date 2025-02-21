N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]

dp[0][0] = 1
for y in range(N):
    for x in range(N):
        step = board[y][x]
        if step == 0:
            continue
        else:
            if y + step < N:
                dp[y + step][x] += dp[y][x]
            if x + step < N:
                dp[y][x + step] += dp[y][x]

print(dp[-1][-1])