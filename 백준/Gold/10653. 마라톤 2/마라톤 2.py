import sys
input = sys.stdin.readline

n, k = map(int, input().split())
checkpoints = [list(map(int, input().split())) for _ in range(n)]

dp = [[float("inf") for _ in range(k + 1)] for _ in range(n)]
dp[0][-1] = 0

def get_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1 - x2) + abs(y1 - y2)

for i in range(n - 1):
    for j in range(k + 1):
        if dp[i][j] == float("inf"):
            continue

        for step in range(j + 1):
            cur = j - step
            next = i + step + 1
            if next >= n:
                break
            dp[next][cur] = min(dp[next][cur], dp[i][j] + get_distance(checkpoints[i], checkpoints[next]))

print(dp[-1][0])