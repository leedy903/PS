import sys
input = sys.stdin.readline

n, m = map(int, input().split())
sequences = [int(input()) for _ in range(n)]

contain = [[0] + [-float('inf')] * m for _ in range(n + 1)]
not_contain = [[0] + [-float('inf')] * m for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, min(m, (i + 1) // 2) + 1):
        not_contain[i][j] = max(contain[i - 1][j], not_contain[i - 1][j])
        contain[i][j] = max(contain[i - 1][j], not_contain[i - 1][j - 1]) + sequences[i - 1]

print(max(contain[n][m], not_contain[n][m]))