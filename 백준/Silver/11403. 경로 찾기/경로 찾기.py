import sys
input = sys.stdin.readline
N = int(input())
adj_matrix = [list(map(int, input().strip().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if adj_matrix[i][k] and adj_matrix[k][j]:
                adj_matrix[i][j] = 1

for i in range(N):
    print(*adj_matrix[i])
